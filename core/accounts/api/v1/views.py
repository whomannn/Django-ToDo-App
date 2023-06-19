from rest_framework import generics
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class SignupApiView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            data = {
                'username' : serializer.validated_data['username'],
                'email' : serializer.validated_data['email']
            }
            serializer.save()
            return Response(data,status=status.HTTP_201_CREATED)
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
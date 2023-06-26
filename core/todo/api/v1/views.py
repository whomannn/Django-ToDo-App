from rest_framework import viewsets
from .serializers import taskSerializer
from todo.models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
class taskModelViewSet(viewsets.ModelViewSet):
    serializer_class = taskSerializer
    queryset = Task.objects.all()
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
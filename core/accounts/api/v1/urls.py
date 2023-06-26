from django.urls import path
from .views import SignupApiView, CustomAuthToken, CustomDiscardAuthToken
from rest_framework_simplejwt import views as jwt_views

app_name = "api-v1"

urlpatterns = [
    path("signup/", SignupApiView.as_view(), name="token-signup"),
    path("api-token-auth/", CustomAuthToken.as_view(), name="api-token-auth"),
    path("logout/", CustomDiscardAuthToken.as_view(), name="token-delete"),
    path(
        "api/token/create/jwt/",
        jwt_views.TokenObtainPairView.as_view(),
        name="create-jwt",
    ),
    path(
        "api/token/refresh/jwt/",
        jwt_views.TokenRefreshView.as_view(),
        name="refresh-jwt",
    ),
    path(
        "api/token/verify/jwt/", jwt_views.TokenVerifyView.as_view(), name="verify-jwt"
    ),
]

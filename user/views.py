from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .serializers import UserSerializer, UserRegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """POST /api/user/register/"""
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(ObtainAuthToken):
    """POST /api/user/login/ → {"token": "..."}"""
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.serializer_class(
            data=request.data, context={"request": request}
        )
        user.is_valid(raise_exception=True)
        token, _ = Token.objects.get_or_create(
            user=user.validated_data["user"]
        )
        return Response({"token": token.key})


class MeView(generics.RetrieveUpdateAPIView):
    """GET/PUT/PATCH /api/user/me/"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

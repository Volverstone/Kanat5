from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, ConfirmSerializer, LoginSerializer
from .models import ConfirmationCode


# Регистрация
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()



class ConfirmView(APIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data["code"]

        try:
            conf = ConfirmationCode.objects.get(code=code)
        except ConfirmationCode.DoesNotExist:
            return Response({"error": "Неверный код"}, status=400)

        user = conf.user
        user.is_active = True
        user.save()

        conf.delete()  # код можно использовать только один раз

        return Response({"message": "Аккаунт подтверждён"})



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        if not user:
            return Response({"error": "Неверные данные"}, status=400)
        if not user.is_active:
            return Response({"error": "Аккаунт не активирован"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

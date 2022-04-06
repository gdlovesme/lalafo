from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Вы успешно зарегистрировались! 
            Вам отправлено письмо с кодом активации.
            """
            return Response(message)

class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Вы успешно автивированы')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]    #проверяем права/
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли')

class ForgotPasswordView(APIView):
    pass

class ChangePasswordView(APIView):
    pass


#REST
# 1. модель клиент-сервер
# 2. отсутствие состояния клиента (то есть сервер не хранит инфу о том какой клиент. все данные клиента будут отправляться во время запроса)
# 3. кеширование (данных, чтобы разгрузить бд)
# 4. единообразие интерфейса (чтобы вьюшки работали одинаковым образом,  и мы получали ответ в одном стиле
# 5. система слоев (приложение может разделяться на слои. то, как работает изнутри , мы этого не видим)
# 6. код по требованию (необязательно) (при запросе, сервер может отправлтяь клиенты код и расширять с его помощью возможности)


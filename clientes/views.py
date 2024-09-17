from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Cliente
from .serializers import ClienteSerializers, LoginSerializers

class RegistroView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializers_class = ClienteSerializers

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cliente = Cliente.objects.get(email=serializer.validated['email'])

        refresh = RefreshToken.for_user(cliente)

        return Response({
            'refresh': str(refresh),
            'acces': str(refresh.access_token)
        })

from rest_framework import serializers
from .models import Cliente
from django.contrib.auth import authenticate


class ClienteSerializers(serializers.ModelSerializers):
    class Meta:
        model = Cliente
        fields = ('id', 'email', 'nome', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        cliente = Cliente(
            email = validated_data['email'],
            nome = validated_data['nome']
        )
        cliente.set_password(validated_data['password'])
        cliente.save()
        return cliente
    
class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        cliente = authenticate(email=email, password=password)

        if not cliente:
            raise serializers.ValidationError('Email ou senha errado')
        
        return{
            'email':cliente.email,
        }
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Cliente(AbstractBaseUser):
    nome = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=120)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

class Menu(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='em preparo')

class Notificacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

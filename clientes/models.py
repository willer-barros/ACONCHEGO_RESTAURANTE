from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, blank=False)
    name_client = models.CharField(max_length=200, null=False, blank=False)
    email_client = models.EmailField(max_length=150, blank=False)
    phone_client = models.CharField(max_length=20, blank=False)
    endereco_client = models.CharField(max_length=150, blank=False)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pedindo', 'Pendindo'),
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendindo')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

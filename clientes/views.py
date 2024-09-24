from rest_framework import generics
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetail(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


def login(request):
    return render(request, 'index.html')


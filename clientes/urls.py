from django.urls import path
from .views import RegistrarClienteView, LoginView, MenuListView, PedidoCreateView, PedidoListView, ListarClientesView

urlpatterns = [
    path('clientes/registrar/', RegistrarClienteView.as_view(), name='registrar-cliente'),
    path('clientes/', ListarClientesView.as_view(), name='todos-clientes'),
    path('clientes/login/', LoginView.as_view(), name='login'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('pedidos/', PedidoCreateView.as_view(), name='criar-pedido'),
    path('pedidos/lista/', PedidoListView.as_view(), name='lista-pedidos'),
]

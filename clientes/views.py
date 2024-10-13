from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Cliente, Menu, Pedido, Notificacao
from .serializers import ClienteSerializer, MenuSerializer, PedidoSerializer, NotificacaoSerializer
from rest_framework.views import APIView
from rest_framework import status

class RegistrarClienteView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

'''
#lembra de apagar apos salvar os dados
class RegistrarClienteView(APIView):
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = ClienteSerializer(data=request.data, many=True)
        else:
            serializer = ClienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class ListarClientesView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = ClienteSerializer

    def post(self, request):
        email = request.data.get('email')
        senha = request.data.get('senha')
        cliente = Cliente.objects.filter(email=email, senha=senha).first()
        if cliente:
            refresh = RefreshToken.for_user(cliente)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Credenciais inválidas'}, status=400)

class MenuListView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class PedidoCreateView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cliente = self.request.user
        serializer.save(cliente=cliente, status='em preparo')

class PedidoListView(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cliente = self.request.user
        return Pedido.objects.filter(cliente=cliente)

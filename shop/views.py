from rest_framework import viewsets
from .serializers import ProductSerializer, TransactionSerializer
from .models import Product, Transaction

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
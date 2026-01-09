from .models import Product, Transaction
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'quantity',
            'created_at',
        ]
    def validate(self, data):
        quantity = data['quantity']
        price = data['price']
        if price <= 0:
            raise serializers.ValidationError('Не коректно введена ціна')
        if quantity < 0:
            raise serializers.ValidationError('Не коректно введене значення')
        return data 

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'items',
            'total_price',
            'status',
            'created_at',
            'updated_at',
        ]
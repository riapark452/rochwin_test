from django.db.models import Sum
from rest_framework import serializers

from core.models import Order


class EmployeeOrdersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    total_amount = serializers.IntegerField()
    total_price = serializers.FloatField()
    clients = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['id', 'full_name', 'total_amount', 'total_price', 'clients']


class ClientOrdersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    total_amount = serializers.IntegerField()
    total_price = serializers.FloatField()

    class Meta:
        model = Order
        fields = ['id', 'full_name', 'total_amount', 'total_price']

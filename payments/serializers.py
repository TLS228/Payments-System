from rest_framework import serializers
from .models import Payment


class BankWebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "operation_id",
            "amount",
            "payer_inn",
            "document_number",
            "document_date"
        ]


class BalanceResponseSerializer(serializers.Serializer):
    inn = serializers.CharField()
    balance = serializers.IntegerField()

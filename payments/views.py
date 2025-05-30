from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BankWebhookSerializer, BalanceResponseSerializer
from .models import Organization
from .services import process_payment


class BankWebhookView(APIView):
    def post(self, request):
        serializer = BankWebhookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        created = process_payment(serializer.validated_data)

        return Response(status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)


class OrganizationBalanceView(APIView):
    def get(self, request, inn):
        try:
            org = Organization.objects.get(inn=inn)
            serializer = BalanceResponseSerializer({"inn": org.inn, "balance": org.balance})
        except Organization.DoesNotExist:
            serializer = BalanceResponseSerializer({"inn": inn, "balance": 0})
        return Response(serializer.data)

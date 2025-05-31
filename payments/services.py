from django.db import transaction
from .models import Organization, Payment, BalanceLog
import logging

logger = logging.getLogger(__name__)


def process_payment(data):
    operation_id = data["operation_id"]

    if Payment.objects.filter(operation_id=operation_id).exists():
        return False

    with transaction.atomic():
        payment = Payment.objects.create(**data)

        org, _ = Organization.objects.get_or_create(inn=payment.payer_inn)
        org.balance += payment.amount
        org.save()

        BalanceLog.objects.create(organization=org, amount=payment.amount)

        logger.info(
            (
                f"[Balance Update] INN {org.inn}: +{payment.amount}, "
                f"New balance: {org.balance}"
            )
        )
        return True

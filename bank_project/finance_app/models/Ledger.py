from django.db import models
from finance_app import models as own_models
from decimal import Decimal


class Ledger(models.Model):
    account = models.ForeignKey("finance_app.Account", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction = models.ForeignKey("finance_app.Transaction", on_delete=models.CASCADE)

    def __str__(self):
        return f"Amount: {self.amount} - Account: {self.account} - Transaction: {self.transaction}"

    @classmethod
    def get_ledgers_with_balances(cls, account):
        ledgers = cls.objects.filter(account=account).order_by(
            "-transaction__transaction_date"
        )
        balance = 0
        for i in range(len(ledgers) - 1, -1, -1):
            balance += ledgers[i].amount
            ledgers[i].balance = balance
        return ledgers

    @classmethod
    def generate_sender_receiver(
        cls,
        sender_account: own_models.Account,
        receiver_account: own_models.Account,
        amount: str,
        transaction_instance: own_models.Transaction,
    ):
        sender_ledger = cls(
            account=sender_account,
            amount=-abs(Decimal(amount)),
            transaction=transaction_instance,
        )

        receiver_ledger = cls(
            account=receiver_account,
            amount=abs(Decimal(amount)),
            transaction=transaction_instance,
        )

        return [sender_ledger, receiver_ledger]

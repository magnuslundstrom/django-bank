from django.contrib.auth.models import User
from django.db import models, transaction
from finance_app import models as own_models
from typing import TypedDict


class post_dict(TypedDict):
    sender_account: str
    account_number: str
    amount: str


class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="receiver"
    )
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sender: {self.sender} - Receiver: {self.receiver} - Date: {self.transaction_date}"

    @classmethod
    def make_transaction(cls, post_dict: post_dict, user):
        try:
            Account = own_models.Account
            Ledger = own_models.Ledger

            sender_account_number = post_dict["sender_account"]
            receiver_account_number = post_dict["account_number"]
            amount = post_dict["amount"]

            sender_account = Account.objects.get(
                account_number=sender_account_number, user=user
            )

            receiver_account = Account.objects.get(
                account_number=receiver_account_number
            )

            transaction_instance = cls(sender=user, receiver=receiver_account.user)

            sender_ledger, receiver_ledger = Ledger.generate_sender_receiver(
                sender_account, receiver_account, amount, transaction_instance
            )

            with transaction.atomic():
                transaction_instance.save()
                sender_ledger.save()
                receiver_ledger.save()

            return True

        except Exception as e:
            return False

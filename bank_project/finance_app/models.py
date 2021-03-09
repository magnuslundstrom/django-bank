from django.db import models
from django.contrib.auth.models import User
import random


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.created_date}"

    def calculate_balance(self, ledgers):
        balance = 0
        for ledger in ledgers:
            balance += ledger.amount
        return balance

    @staticmethod
    def generate_account_number():
        accounts = Account.objects.all()

        while True:
            found = False
            account_number = random.randint(10000000000000, 99999999999999)
            for account in accounts:
                if account.account_number == account_number:
                    found = True
                    break

            if not found:
                break

        return account_number


class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="receiver"
    )
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sender: {self.sender} - Receiver: {self.receiver} - Date: {self.transaction_date} "


class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Amount: {self.amount} - Account: {self.account} - Transaction: {self.transaction}"

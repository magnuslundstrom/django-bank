from django.contrib.auth.models import User
from django.db import models
import random
from finance_app import models as own_models


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.created_date}"

    @classmethod
    def generate_account_number(cls):
        accounts = cls.objects.all()
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

    @classmethod
    def get_accounts_with_balances(cls, user):
        def calculate_balance(ledgers):
            balance = 0
            for ledger in ledgers:
                balance += ledger.amount
            return balance

        accounts = cls.objects.all().filter(user=user)
        for account in accounts:
            ledgers = own_models.Ledger.objects.filter(account=account)
            if not ledgers:
                account.balance = 0
            else:
                account.balance = calculate_balance(ledgers)
        return accounts
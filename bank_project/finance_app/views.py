from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account, Ledger, Transaction
from operator import itemgetter
from decimal import Decimal
from django.db import transaction


@login_required
def display_costumer_accounts(request):
    accounts = Account.objects.filter(user=request.user)
    return render(
        request, "finance_app/display_costumer_accounts.html", {"accounts": accounts}
    )


@login_required
def create_new_account_number(request):
    account = Account(
        user=request.user, account_number=Account.generate_account_number()
    )
    account.save()
    return redirect("costumer_app:display_costumer_accounts")


@login_required
def display_account_transactions(request, account_number):
    account = Account.objects.get(account_number=account_number)
    ledgers = Ledger.objects.filter(account__account_number=account_number).order_by(
        "-transaction__transaction_date"
    )

    # If I do for ledge in ledgers, it will only create a shallow copy, not sticking to the ledgers list?
    balance = 0
    for i in range(len(ledgers) - 1, -1, -1):
        balance += ledgers[i].amount
        ledgers[i].balance = balance

    context = {"account_number": account.account_number, "ledgers": ledgers}
    return render(request, "finance_app/display_account_transfers.html", context)


@login_required
def make_transfer(request):
    context = {"owned_accounts": Account.objects.filter(user=request.user)}

    if request.method == "POST":
        sender_account, receiver_account, amount = itemgetter(
            "sender_account", "account_number", "amount"
        )(request.POST)

        try:
            sender_account = Account.objects.get(
                account_number=sender_account, user=request.user
            )
            receiver_account = Account.objects.get(account_number=receiver_account)
        except:
            context["error"] = "No such account number"
            return render(request, "transactions_app/transfer.html", context)

        try:
            transaction_instance = Transaction()
            sender_ledger = Ledger(
                account=sender_account,
                amount=-abs(Decimal(amount)),
                transaction=transaction_instance,
            )

            receiver_ledger = Ledger(
                account=receiver_account,
                amount=abs(Decimal(amount)),
                transaction=transaction_instance,
            )

            transaction_instance.sender = sender_account.user
            transaction_instance.receiver = receiver_account.user

            with transaction.atomic():
                transaction_instance.save()
                sender_ledger.save()
                receiver_ledger.save()

        except Exception as e:
            context["error"] = "Something went wrong, you might want to try again."

    return render(request, "finance_app/make_transfer.html", context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction, Account, Ledger


@login_required
def display_costumer_accounts(request):
    accounts = Account.get_accounts_with_balances(request.user)
    return render(
        request,
        "finance_app/display_costumer_accounts.html",
        {"accounts": accounts},
    )


@login_required
def create_new_account_number(request):
    account = Account(
        user=request.user, account_number=Account.generate_account_number()
    )
    account.save()
    return redirect("costumer_app:display_costumer_accounts")


# Should check if the request.user has permissions
@login_required
def display_account_transactions(request, account_number):
    account = Account.objects.get(account_number=account_number)
    ledgers = Ledger.get_ledgers_with_balances(account)
    context = {"account_number": account.account_number, "ledgers": ledgers}
    return render(request, "finance_app/display_account_transfers.html", context)


@login_required
def make_transfer(request):
    context = {"owned_accounts": Account.objects.filter(user=request.user)}

    if request.method == "POST":
        status = Transaction.make_transaction(request.POST, request.user)
        if not status:
            context[
                "message"
            ] = "Something went wrong, please double check the account number"
        else:
            context["message"] = "Money transfered!"

    return render(request, "finance_app/make_transfer.html", context)
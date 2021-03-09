from django.urls import path
from . import views
from finance_app import views as finance_views
from loan_app import views as loan_views

app_name = "costumer_app"

urlpatterns = [
    path("", finance_views.display_costumer_accounts, name="display_costumer_accounts"),
    path("make-transfer", finance_views.make_transfer, name="make_transfer"),
    path(
        "transactions/<int:account_number>",
        finance_views.display_account_transactions,
        name="display_account_transactions",
    ),
    path("loans", loan_views.costumer_loan_overview, name="costumer_loan_overview"),
]

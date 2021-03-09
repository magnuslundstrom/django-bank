from django.urls import path
from . import views

app_name = "loan_app"

urlpatterns = [
    # path("", views.costumer_loan_overview, name="costumer_loan_overview"),
    # path("create", views.create, name="create"),
    # path("loan-types", views.loan_types, name="loan_types"),
    # path("loan-types/delete", views.delete, name="delete"),
    path(
        "delete-loan-application",
        views.delete_loan_application,
        name="delete_loan_application",
    ),
    path("delete-loan-type", views.delete_loan_type, name="delete_loan_type"),
]

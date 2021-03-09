from django.urls import path
from . import views

app_name = "loan_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("loan-types", views.loan_types, name="loan_types"),
    path("loan-types/delete", views.delete, name="delete"),
    path("apply/<int:id>", views.apply, name="apply"),
    path(
        "delete-loan-application",
        views.delete_loan_application,
        name="delete_loan_application",
    ),
]

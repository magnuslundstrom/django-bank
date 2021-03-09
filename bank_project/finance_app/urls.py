from django.urls import path
from . import views


app_name = "finance_app"

urlpatterns = [
    path(
        "/create-new-account-number",
        views.create_new_account_number,
        name="create_new_account_number",
    ),
]

from django.urls import path
from . import views

app_name = "account_app"

urlpatterns = [
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("costumer-signup", views.costumer_signup, name="costumer_signup"),
]

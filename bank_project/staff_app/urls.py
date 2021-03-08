from django.urls import path
from . import views

app_name = "staff_app"

urlpatterns = [
    path("", views.overview, name="overview"),
]

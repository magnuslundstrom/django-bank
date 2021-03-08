from django.urls import path
from . import views

app_name = "super_app"
urlpatterns = [
    path("", views.show_staff, name="show_staff"),
    path("create-staff", views.create_staff, name="create_staff"),
    path("delete-staff/<int:staff_id>", views.delete_staff, name="delete_staff"),
]

from django.urls import path
from . import views


app_name = "staff_app"

urlpatterns = [
    path("", views.overview, name="overview"),
    path("manage-ranks", views.manage_ranks, name="manage_ranks"),
    path("costumers", views.display_costumers, name="display_costumers"),
    path(
        "change-costumer-rank/<int:costumer_id>",
        views.change_costumer_rank,
        name="change_costumer_rank",
    ),
    path(
        "delete-costumer/<int:costumer_id>",
        views.delete_costumer,
        name="delete_costumer",
    ),
]

from django.urls import path
from . import views
from loan_app import views as loan_views

app_name = "staff_app"

urlpatterns = [
    path("", views.overview, name="overview"),
    # rank related stuff
    path("manage-ranks", views.manage_ranks, name="manage_ranks"),
    path(
        "change-costumer-rank/<int:costumer_id>",
        views.change_costumer_rank,
        name="change_costumer_rank",
    ),
    # costumer related stuff
    path("costumers", views.display_costumers, name="display_costumers"),
    path(
        "delete-costumer/<int:costumer_id>",
        views.delete_costumer,
        name="delete_costumer",
    ),
    # Loan Related stuff
    path("loans", loan_views.display_loan_types, name="display_loan_types"),
    path("loans/type/create", loan_views.create_loan_type, name="create_loan_type"),
    path(
        "loans/loan-applications",
        loan_views.display_loan_applications,
        name="display_loan_applications",
    ),
    path(
        "loans/approve-loan-application",
        loan_views.approve_loan_application,
        name="approve_loan_application",
    ),
]

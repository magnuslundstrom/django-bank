# Written by Magnus Lundstrøm
from costumer_app.models import Costumer
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import LoanTypeForm, LoanApplicationForm
from .models import Loan, LoanType, LoanApplication
from django.contrib.auth.decorators import login_required
from operator import itemgetter

# needs to fetch approved loans too
@login_required
def costumer_loan_overview(request):
    costumer = Costumer.objects.get(user=request.user)
    loan_applications = LoanApplication.objects.filter(user=request.user, status=False)
    loan_types = LoanType.objects.all()
    active_loans = Loan.objects.filter(user=request.user)

    context = {
        "costumer": costumer,
        "user_loans": [],
        "loan_types": loan_types,
        "loan_applications": loan_applications,
        "active_loans": active_loans,
    }
    return render(request, "loan_app/costumer_loan_overview.html", context)


# TODO: ADD RANKING CHECK + RENAME TO LOAN_TYPE_CREATE
@login_required
def create_loan_type(request):
    form = LoanTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LoanTypeForm()

    context = {"form": form}
    return render(request, "loan_app/create_loan_type.html", context)


@login_required
def display_loan_types(request):
    loan_types = LoanType.objects.all()
    context = {"loan_types": loan_types}
    return render(request, "loan_app/loan_types.html", context)


@login_required
def delete_loan_type(request):
    if request.method == "POST":
        loan_type_id = request.POST["loan_type_id"]
        type = LoanType.objects.get(id=loan_type_id)
        type.delete()
    return redirect(reverse("staff_app:display_loan_types"))


# SHOULD PROBABLY CHECK IF THE USER IS ALLOWED TO GO HERE LATER DUE TO RANKING
@login_required
def apply_loan(request, loan_id):
    context = {}
    loan_type = LoanType.objects.get(id=loan_id)
    if request.method == "POST":
        requested_loan_amount = itemgetter("requested_loan_amount")(request.POST)

        if not loan_type.validate_requested_amount(requested_loan_amount):
            context[
                "message"
            ] = "Please select a value between the min and max boundries."

        else:
            application = LoanApplication(
                user=request.user,
                loan_type=loan_type,
                requested_loan_amount=requested_loan_amount,
            )
            application.save()

            context[
                "message"
            ] = "Your loan has been requested. We will get back to you as soon as possible."

    form = LoanApplicationForm()
    context["loan_type"] = loan_type
    context["loan_application_form"] = form
    return render(request, "loan_app/costumer_loan_apply.html", context)


# for staff members too approve and not
@login_required
def display_loan_applications(request):
    loan_applications = LoanApplication.objects.filter(status=False)
    return render(
        request,
        "loan_app/display_loan_applications.html",
        {"loan_applications": loan_applications},
    )


# TODO: ADD RANKING CHECK
@login_required
def delete_loan_application(request):
    if request.method == "POST":
        application_id = request.POST["application_id"]
        loan_application = LoanApplication.objects.get(id=application_id)
        if loan_application.user == request.user:
            loan_application.delete()

    if request.user.is_staff:
        return redirect(reverse("staff_app:display_loan_applications"))
    else:
        return redirect(reverse("costumer_app:costumer_loan_overview"))


@login_required
def approve_loan_application(request):
    if request.method == "POST":

        application_id = request.POST["application_id"]
        loan_application = LoanApplication.objects.get(id=application_id)
        loan_application.status = True
        loan_application.save()

        loan = Loan(
            user=loan_application.user,
            amount=loan_application.requested_loan_amount,
            loan_type=loan_application.loan_type,
        )
        loan.save()

    return redirect(reverse("staff_app:display_loan_applications"))
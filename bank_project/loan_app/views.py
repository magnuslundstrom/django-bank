# Written by Magnus Lundstrøm
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import LoanTypeForm, LoanApplicationForm
from .models import Loan, LoanType, LoanApplication
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from operator import itemgetter

# needs to fetch approved loans too
@login_required
def costumer_loan_overview(request):
    loan_applications = LoanApplication.objects.all().filter(user=request.user)
    loan_types = LoanType.objects.all()
    context = {
        "user_loans": [],
        "loan_types": loan_types,
        "loan_applications": loan_applications,
    }
    return render(request, "loan_app/costumer_loan_overview.html", context)


# TODO: ADD RANKING CHECK + RENAME TO LOAN_TYPE_CREATE
@login_required
def create(request):
    form = LoanTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LoanTypeForm()

    context = {"form": form}
    return render(request, "loan_app/create.html", context)


@login_required
def loan_types(request):
    if request.method == "POST":
        pass
    loan_types = LoanType.objects.all()

    context = {"loan_types": loan_types}
    return render(request, "loan_app/loan_types.html", context)


# TODO: ADD RANKING CHECK + RENAME TO LOAN_TYPE_DELETE
@login_required
def delete(request):
    if request.method == "POST":
        loan_type_id = request.POST["loan_type_id"]
        type = LoanType.objects.get(id=loan_type_id)
        type.delete()

    return redirect(reverse("loan_app:loan_types"))


# SHOULD PROBABLY CHECK IF THE USER IS ALLOWED TO GO HERE LATER DUE TO RANKING
@login_required
def apply(request, id):
    context = {}
    loan_type = LoanType.objects.get(id=id)
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
    return render(request, "loan_app/apply.html", context)


# TODO: ADD RANKING CHECK
@login_required
def delete_loan_application(request):
    if request.method == "POST":
        application_id = request.POST["application_id"]
        loan_application = LoanApplication.objects.get(id=application_id)
        if loan_application.user == request.user:
            loan_application.delete()

    return redirect(reverse("loan_app:index"))


# for staff members too approve and not
@login_required
def view_loan_applications(request):
    pass
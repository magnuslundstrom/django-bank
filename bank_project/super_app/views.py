# Written by Magnus Lundstrøm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CreateStaffForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from operator import itemgetter


# TODO ~ Validation
@login_required
def show_staff(request):
    staff_members = User.objects.filter(is_staff=True, is_superuser=False)
    return render(
        request, "super_app/show_staff.html", {"staff_members": staff_members}
    )


@login_required
def create_staff(request):
    form = CreateStaffForm()

    if request.method == "POST":
        username, password, first_name, last_name, email = itemgetter(
            "username", "password", "first_name", "last_name", "email"
        )(request.POST)

        User.objects.create_user(
            username=username,
            password=password,
            is_staff=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        return redirect(reverse("super_app:show_staff"))

    return render(request, "super_app/create_staff.html", {"form": form})


@login_required
def delete_staff(request, staff_id):
    staff = User.objects.get(id=staff_id)
    staff.delete()

    return redirect(reverse("super_app:show_staff"))

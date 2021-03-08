# Written by Magnus Lundstrøm
from django.shortcuts import render, redirect
from .forms import CreateStaffForm
from django.urls import reverse
from django.contrib.auth.models import User


# TODO ~ Validation
def show_staff(request):
    staff_members = User.objects.filter(is_staff=True, is_superuser=False)
    print(staff_members)
    return render(
        request, "super_app/show_staff.html", {"staff_members": staff_members}
    )


def create_staff(request):
    form = CreateStaffForm()
    if request.method == "POST":
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect(reverse("super_app:show_staff"))

    return render(request, "super_app/create_staff.html", {"form": form})


def delete_staff(request, staff_id):
    staff = User.objects.get(id=staff_id)
    staff.delete()

    return redirect(reverse("super_app:show_staff"))

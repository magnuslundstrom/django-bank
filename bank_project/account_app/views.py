from costumer_app.models import Costumer, Rank
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as dj_login,
    logout as dj_logout,
)
from .forms import LoginForm, CreateCostumerForm
from django.urls import reverse
from operator import itemgetter
from django.db import transaction


def login(request):
    context = {"form": LoginForm()}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            dj_login(request, user)
            # add redirections here later
            if user.is_superuser:
                return redirect(reverse("super_app:show_staff"))
            elif user.is_staff:
                return redirect(reverse("staff_app:overview"))
            else:
                return redirect(reverse("costumer_app:display_costumer_accounts"))
        else:
            context["error"] = "Wrong email or password"
        return render(request, "account_app/login.html", context)

    return render(request, "account_app/login.html", context)


def logout(request):
    dj_logout(request)
    return redirect(reverse("account_app:login"))


def costumer_signup(request):
    form = CreateCostumerForm()

    if request.method == "POST":
        username, password, first_name, last_name, email = itemgetter(
            "username", "password", "first_name", "last_name", "email"
        )(request.POST)
        with transaction.atomic():

            user = User.objects.create_user(
                username=username,
                password=password,
                is_staff=False,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            rank = Rank.objects.get(name="Basic")
            costumer = Costumer(user=user, rank=rank)
            costumer.save()

        return redirect(reverse("account_app:login"))
    return render(request, "account_app/signup.html", {"form": form})

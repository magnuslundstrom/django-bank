from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as dj_login,
    logout as dj_logout,
)
from .forms import LoginForm
from django.urls import reverse


def login(request):

    if request.method == "POST":
        context = {}
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            # add redirections here later
            if user.is_superuser:
                return redirect(reverse("super_app:show_staff"))
        else:
            context["error"] = "Wrong email or password"
        return render(request, "account_app/login.html", context)

    form = LoginForm()
    return render(request, "account_app/login.html", {"form": form})


def logout(request):
    dj_logout(request)
    return redirect(reverse("account_app:login"))

from django.shortcuts import render, redirect


def overview(request):
    return render(request, "costumer_app/overview.html")

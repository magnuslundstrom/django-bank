from django.shortcuts import render


def overview(request):
    return render(request, "staff_app/overview.html")
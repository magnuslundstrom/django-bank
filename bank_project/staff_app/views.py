from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateRankForm
from costumer_app.models import Rank, Costumer


@login_required
def overview(request):
    return render(request, "staff_app/overview.html")


# for now can only create and not delete
@login_required
def manage_ranks(request):
    form = CreateRankForm()
    if request.method == "POST":
        form = CreateRankForm(request.POST)
        if form.is_valid():
            form.save()

    ranks = Rank.objects.all()
    return render(
        request, "staff_app/manage_ranks.html", {"form": form, "ranks": ranks}
    )


@login_required
def display_costumers(request):
    costumers = Costumer.objects.all()

    return render(request, "staff_app/display_costumers.html", {"costumers": costumers})

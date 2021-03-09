from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateRankForm, ChangeCostumerRankForm
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


@login_required
def change_costumer_rank(request, costumer_id):
    costumer = Costumer.objects.get(id=costumer_id)
    form = ChangeCostumerRankForm(initial={"rank": costumer.rank})
    if request.method == "POST":
        form = ChangeCostumerRankForm(request.POST, instance=costumer)
        if form.is_valid():
            form.save()
            return redirect(reverse("staff_app:display_costumers"))

    return render(
        request,
        "staff_app/change_costumer_rank.html",
        {"costumer": costumer, "form": form},
    )


@login_required
def delete_costumer(request, costumer_id):
    costumer = Costumer.objects.get(id=costumer_id)
    name = ""
    if costumer:
        name = costumer.user.first_name
        costumer.user.delete()

    return render(
        request,
        "staff_app/display_costumers.html",
        {"message": f"{name} was deleted"},
    )

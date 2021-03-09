from django import forms
from costumer_app.models import Rank, Costumer


class CreateRankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = "__all__"


class ChangeCostumerRankForm(forms.ModelForm):
    rank = forms.ModelChoiceField(queryset=Rank.objects.all())

    class Meta:
        model = Costumer
        fields = ["rank"]

from django import forms
from costumer_app.models import Rank


class CreateRankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = "__all__"

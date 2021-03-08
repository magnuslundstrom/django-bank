from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class CreateCostumerForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=255)

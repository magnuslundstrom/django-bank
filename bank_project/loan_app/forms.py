from django import forms
from .models import LoanType, LoanApplication


class LoanTypeForm(forms.ModelForm):
    class Meta:
        model = LoanType
        fields = ["loan_name", "max_amount", "min_amount", "requires_approval", "rate"]


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ["requested_loan_amount"]

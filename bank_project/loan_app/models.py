# written by Magnus Lundstrøm

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Loan(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"User: {self.user_fk} - Amount: {self.amount}"

    # implement later -- Should return if the loan is paid back or not
    def getStatus():
        pass

    # implement later -- Should return the amount left
    def calculateAmountLeft():
        pass


class LoanType(models.Model):
    loan_name = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    max_amount = models.DecimalField(max_digits=20, decimal_places=2)
    min_amount = models.DecimalField(max_digits=20, decimal_places=2)
    requires_approval = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.loan_name} - Rate: {self.rate} - Max: {self.max_amount} - Min: {self.min_amount} - approval: {self.requires_approval}"

    def validate_requested_amount(self, requested_amount):
        requested_amount = Decimal(requested_amount)
        if requested_amount < self.min_amount or requested_amount > self.max_amount:
            return False
        else:
            return True


class LoanApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.DO_NOTHING)
    requested_loan_amount = models.DecimalField(max_digits=20, decimal_places=2)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Applicant: {self.user} - Requested amount: {self.requested_loan_amount} - status: {self.status} - Loan type: {self.loan_type}"

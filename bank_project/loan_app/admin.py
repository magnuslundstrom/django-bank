from django.contrib import admin
from .models import Loan, LoanType, LoanApplication

admin.site.register(Loan)
admin.site.register(LoanType)
admin.site.register(LoanApplication)

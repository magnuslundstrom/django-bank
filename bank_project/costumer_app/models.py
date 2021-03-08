from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rank(models.Model):
    name = models.CharField(max_length=20, unique=True)
    can_loan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.can_loan}"


class Costumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, default="")
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.user} - {self.phone_number} - {self.rank}"

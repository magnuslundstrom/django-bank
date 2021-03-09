# Generated by Django 3.1.6 on 2021-03-09 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=200)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('min_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('requires_approval', models.BooleanField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_loan_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('loan_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loan_app.loantype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
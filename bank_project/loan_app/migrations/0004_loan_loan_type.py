# Generated by Django 3.1.6 on 2021-03-09 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0003_auto_20210309_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='loan_app.loantype'),
        ),
    ]

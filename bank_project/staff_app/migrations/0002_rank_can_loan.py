# Generated by Django 3.1.6 on 2021-03-08 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='can_loan',
            field=models.BooleanField(default=False),
        ),
    ]

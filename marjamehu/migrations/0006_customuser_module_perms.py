# Generated by Django 2.0 on 2018-04-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marjamehu', '0005_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='module_perms',
            field=models.BooleanField(default=True),
        ),
    ]

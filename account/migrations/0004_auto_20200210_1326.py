# Generated by Django 3.0.2 on 2020-02-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200208_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='last Name'),
        ),
    ]

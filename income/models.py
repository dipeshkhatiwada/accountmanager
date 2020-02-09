from django.db import models
from abstract.models import Category, Abs


# Create your models here.

class IncomeCategoryManager(models.Manager):
    pass


class IncomeCategory(Category):
    objects = IncomeCategoryManager()

    class Meta:
        db_table = 'income_category'


class IncomeManager(models.Manager):
    pass


class Income(Abs):
    image = models.ImageField(upload_to='income/', null=True, blank=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)

    objects = IncomeCategoryManager()

    class Meta:
        db_table = 'income'

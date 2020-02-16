import datetime

from django.db import models
from django.db.models import Sum

from abstract.models import Category, Abs


# Create your models here.

class ExpensesCategoryManager(models.Manager):
    pass


class ExpensesCategory(Category):
    objects = ExpensesCategoryManager()
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'expenses_category'


class ExpensesManager(models.Manager):
    def getCurrentDayExpenses(self, user_id):
        return self.filter(
            date=datetime.date.today(),
            category__in=ExpensesCategory.objects.filter(user_id=user_id)
        ).aggregate(Sum('price'))


class Expenses(Abs):
    image = models.ImageField(upload_to='expenses/', null=True, blank=True)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE)

    objects = ExpensesManager()

    class Meta:
        db_table = 'expenses'

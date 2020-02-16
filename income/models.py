from django.db import models
from abstract.models import Category, Abs
from django.db.models import Sum, Count
import datetime
from datetime import timedelta


# Create your models here.

class IncomeCategoryManager(models.Manager):
    def getAllCategory(self, user_id):
        return self.filter(user_id=user_id)


class IncomeCategory(Category):
    objects = IncomeCategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'income_category'


class IncomeManager(models.Manager):
    def getCurrentMonthIncome(self, user_id):
        return self.filter(
            date__month=datetime.date.today().month,
            date__year=datetime.date.today().year,
            category__in=IncomeCategory.objects.filter(user_id=user_id)
        ).aggregate(Sum('price'))

    def getCurrentDayIncome(self, user_id):
        return self.filter(
            date=datetime.date.today(),
            category__in=IncomeCategory.objects.filter(user_id=user_id)
        ).aggregate(Sum('price'))

    def getYesterdayIncome(self, user_id):
        yesterday = datetime.datetime.today() - timedelta(days=1)
        return self.filter(
            date=yesterday,
            category__in=IncomeCategory.objects.filter(user_id=user_id)
        ).aggregate(Sum('price'))

    def getLastMonthIncome(self, user_id):
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        pervmonth = month - 1
        if pervmonth == 0:
            pervmonth = 12
            year = year - 1
        return self.filter(
            date__month=pervmonth,
            date__year=year,
            category__in=IncomeCategory.objects.filter(user_id=user_id)
        ).aggregate(Sum('price'))
    def getIncomeByCategory(self,user_id):
        all_category = IncomeCategory.objects.getAllCategory(user_id)
        bycategory = {}
        for cat in all_category:
            x = self.filter(category=cat).aggregate(Sum('price'))
            bycategory[cat.title]=x['price__sum']
        return bycategory
    def countIncomeByCategory(self,user_id):
        all_category = IncomeCategory.objects.getAllCategory(user_id)
        bycategory = {}
        for cat in all_category:
            x = self.filter(category=cat).aggregate(Count('price'))
            bycategory[cat.title]=x['price__count']
        return bycategory


class Income(Abs):
    image = models.ImageField(upload_to='income/', null=True, blank=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)

    objects = IncomeManager()

    class Meta:
        db_table = 'income'

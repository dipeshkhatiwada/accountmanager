from rest_framework import serializers
from income.models import IncomeCategory,Income

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =IncomeCategory
        fields = ['id','title',]

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Income
        fields = [
            'id','title','price','description','category'
        ]
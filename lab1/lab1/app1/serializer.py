from rest_framework import serializers
from .models import Employee, Product, ShoppingCenter


class EmployeeSerializer(serializers.ModelSerializer):
    employee_firstname = serializers.CharField(max_length=50)
    employee_lastname = serializers.CharField(max_length=50)
    employee_salary = serializers.FloatField()
    employee_age = serializers.IntegerField()
    employee_phone = serializers.IntegerField()
    employee_shop = ShoppingCenter()
    class Meta:
        model = Employee
        fields = "__all__"



class EmployeeIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = "__all__"
        fields = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ShoppingCenterIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCenter
        #fields = "__all__"
        fields=("id",)

class ShoppingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCenter
        fields = "__all__"





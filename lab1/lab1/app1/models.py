from django.db import models

# Create your models here.

class ShoppingCenter(models.Model):
    shop_code= models.IntegerField()
    shop_name= models.CharField(max_length=50)
    shop_category= models.CharField(max_length=50)
    nr_employee= models.IntegerField()
    shop_floor= models.IntegerField()

    def __str__(self):
        return f"{self.shop_code} -- {self.shop_name}"

class Employee(models.Model):
    employee_firstname= models.CharField(max_length=50)
    employee_lastname = models.CharField(max_length=50)
    employee_salary= models.FloatField()
    employee_age= models.IntegerField()
    employee_phone=models.IntegerField()
    employee_shop=models.ForeignKey(ShoppingCenter,on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.employee_firstname} {self.employee_lastname}  -- {self.employee_shop}"

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    product_price = models.FloatField()
    product_pieces= models.IntegerField()
    product_color = models.CharField(max_length=30)


    def __str__(self):
        return f"{self.product_name} -- {self.product_price}"






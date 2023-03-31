# Generated by Django 4.1.7 on 2023-03-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_shoppingcenter_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shopping_center',
            field=models.ManyToManyField(through='app1.ShoppingCenter_Product', to='app1.shoppingcenter'),
        ),
        migrations.AddField(
            model_name='shoppingcenter',
            name='products',
            field=models.ManyToManyField(through='app1.ShoppingCenter_Product', to='app1.product'),
        ),
    ]

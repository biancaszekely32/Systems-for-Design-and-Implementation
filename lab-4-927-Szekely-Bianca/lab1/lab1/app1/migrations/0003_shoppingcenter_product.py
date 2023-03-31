# Generated by Django 4.1.7 on 2023-03-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_product_product_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCenter_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('availability', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.shoppingcenter')),
            ],
        ),
    ]

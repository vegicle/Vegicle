# Generated by Django 3.0.5 on 2020-06-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Prices',
        ),
        migrations.AddField(
            model_name='product',
            name='prices',
            field=models.ManyToManyField(to='shop.Prices'),
        ),
    ]

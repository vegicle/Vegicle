# Generated by Django 3.0.8 on 2020-07-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_item_gms'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='product_varient_id',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_item_gms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gms',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
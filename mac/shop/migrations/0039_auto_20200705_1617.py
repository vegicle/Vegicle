# Generated by Django 3.0.8 on 2020-07-05 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_auto_20200704_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varients',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varients', to='shop.Product'),
        ),
    ]

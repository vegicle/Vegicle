# Generated by Django 3.0.5 on 2020-07-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_remove_varients_p_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='varients',
            name='gms',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='varients',
            name='price',
            field=models.CharField(blank=True, help_text='The price of product', max_length=50),
        ),
    ]
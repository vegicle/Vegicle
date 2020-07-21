# Generated by Django 3.0.5 on 2020-06-15 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price_five',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_four',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_one',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_three',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_two',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-07 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200705_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='gms',
        ),
    ]
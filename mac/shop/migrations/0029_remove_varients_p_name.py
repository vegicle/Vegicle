# Generated by Django 3.0.5 on 2020-07-01 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20200701_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='varients',
            name='p_name',
        ),
    ]

# Generated by Django 3.0.5 on 2020-06-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20200618_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
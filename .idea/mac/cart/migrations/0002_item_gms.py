# Generated by Django 3.0.8 on 2020-07-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gms',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
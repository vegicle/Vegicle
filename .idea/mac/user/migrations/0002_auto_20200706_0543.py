# Generated by Django 3.0.5 on 2020-07-06 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='country',
            new_name='state',
        ),
    ]

# Generated by Django 3.0.5 on 2020-07-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0044_auto_20200707_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

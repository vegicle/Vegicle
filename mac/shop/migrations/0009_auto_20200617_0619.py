# Generated by Django 3.0.5 on 2020-06-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200617_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='prices',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]

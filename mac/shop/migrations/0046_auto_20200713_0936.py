# Generated by Django 3.0.8 on 2020-07-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_instruction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='instruction',
        ),
        migrations.AddField(
            model_name='instruction',
            name='instruction_message',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='instruction',
            name='min_coast',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Minimal coast of something', max_digits=10),
        ),
    ]

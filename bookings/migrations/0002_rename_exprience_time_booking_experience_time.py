# Generated by Django 4.1.1 on 2022-10-24 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='exprience_time',
            new_name='experience_time',
        ),
    ]

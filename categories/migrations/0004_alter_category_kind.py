# Generated by Django 4.1.1 on 2022-10-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='kind',
            field=models.CharField(choices=[('rooms', 'Rooms'), ('experiences', 'Experience')], max_length=15),
        ),
    ]
# Generated by Django 3.2.4 on 2023-02-07 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0032_booking_booking_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_list',
            name='book',
        ),
    ]

# Generated by Django 3.2.4 on 2023-02-07 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0046_alter_booking_list_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_list',
            name='book',
        ),
    ]

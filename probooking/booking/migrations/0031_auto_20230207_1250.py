# Generated by Django 3.2.4 on 2023-02-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0030_booking_list_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_list',
            name='book',
        ),
        migrations.DeleteModel(
            name='booking',
        ),
        migrations.DeleteModel(
            name='booking_list',
        ),
    ]

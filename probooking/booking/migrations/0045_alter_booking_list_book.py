# Generated by Django 3.2.4 on 2023-02-07 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0044_alter_booking_list_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_list',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
    ]

# Generated by Django 3.2.4 on 2023-02-06 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20230205_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_list',
            name='Book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
            preserve_default=False,
        ),
    ]
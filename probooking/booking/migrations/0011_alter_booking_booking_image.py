# Generated by Django 3.2.4 on 2023-02-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20230204_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
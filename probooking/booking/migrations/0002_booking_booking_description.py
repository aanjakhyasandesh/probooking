# Generated by Django 3.2.4 on 2023-01-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_description',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2023-02-06 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_discount_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount_token',
            name='token',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

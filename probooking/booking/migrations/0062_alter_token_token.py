# Generated by Django 3.2.4 on 2023-02-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0061_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=4),
        ),
    ]

# Generated by Django 3.2.4 on 2023-02-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0053_booking_list_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]

# Generated by Django 3.2.4 on 2023-02-07 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0049_auto_20230207_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('booking_image', models.ImageField(upload_to='')),
                ('booking_title', models.CharField(max_length=50)),
                ('booking_description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'booking',
            },
        ),
        migrations.CreateModel(
            name='booking_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14)),
                ('date', models.CharField(max_length=12)),
                ('time', models.CharField(max_length=8)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
            ],
            options={
                'verbose_name_plural': 'bookinglist',
            },
        ),
    ]
# Generated by Django 3.2.4 on 2021-09-05 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourway', '0004_auto_20210905_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ways_describe',
            old_name='description',
            new_name='way_description',
        ),
        migrations.RenameField(
            model_name='ways_describe',
            old_name='image',
            new_name='way_image',
        ),
        migrations.RenameField(
            model_name='ways_describe',
            old_name='title',
            new_name='way_title',
        ),
    ]
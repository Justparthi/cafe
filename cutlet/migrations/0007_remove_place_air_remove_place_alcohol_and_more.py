# Generated by Django 5.1 on 2024-09-23 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cutlet', '0006_rename_test_place_stable_wifi_place_air_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='air',
        ),
        migrations.RemoveField(
            model_name='place',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='place',
            name='light',
        ),
        migrations.RemoveField(
            model_name='place',
            name='outdoor',
        ),
        migrations.RemoveField(
            model_name='place',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='place',
            name='pet',
        ),
        migrations.RemoveField(
            model_name='place',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='place',
            name='smoke_free',
        ),
        migrations.RemoveField(
            model_name='place',
            name='spacious',
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutlet', '0002_alter_place_img_url_alter_place_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='can_take_calls',
            field=models.CharField(max_length=6969),
        ),
        migrations.AlterField(
            model_name='place',
            name='has_sockets',
            field=models.CharField(max_length=6969),
        ),
        migrations.AlterField(
            model_name='place',
            name='has_toilet',
            field=models.CharField(max_length=6969),
        ),
        migrations.AlterField(
            model_name='place',
            name='has_wifi',
            field=models.CharField(max_length=6969),
        ),
        migrations.AlterField(
            model_name='place',
            name='seats',
            field=models.CharField(max_length=255),
        ),
    ]

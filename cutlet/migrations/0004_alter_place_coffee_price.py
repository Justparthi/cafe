# Generated by Django 5.1.1 on 2024-09-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutlet', '0003_alter_place_can_take_calls_alter_place_has_sockets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coffee_price',
            field=models.CharField(max_length=255),
        ),
    ]
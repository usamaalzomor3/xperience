# Generated by Django 4.2.13 on 2024-05-25 17:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_remove_carreservationoption_final_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreservation',
            name='dropoff_adress',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carreservation',
            name='dropoff_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='carreservation',
            name='pickup_adress',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carreservation',
            name='pickup_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='hotelreservation',
            name='adress',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelreservation',
            name='locaion_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='dropoff_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='pickup_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='hotelreservation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(help_text='unique tracking number', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(help_text='Address, State, Postal Code, County')),
                ('creation_date', models.DateTimeField()),
                ('destination', models.TextField(help_text='Address, State, Postal Code, County')),
                ('arrival_date', models.DateTimeField()),
                ('quantity', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dimensions', models.CharField(help_text='0.9m x 1.5m x 3.0m', max_length=20)),
                ('ship_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ship_info', to='app.Shipment')),
            ],
        ),
        migrations.CreateModel(
            name='ShipStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('col', 'Collecting'), ('pro', 'Processing'), ('trn', 'In Transit'), ('del', 'Delivering'), ('dld', 'Delivered')], default='col', max_length=3)),
                ('ship_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='app.Shipment')),
            ],
        ),
        migrations.CreateModel(
            name='StatusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_status_date', models.DateTimeField()),
                ('current_location', models.CharField(help_text='State and Country', max_length=30)),
                ('action', models.CharField(help_text='current state of shipment', max_length=400)),
                ('ship_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_info', to='app.Shipment')),
                ('this_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infostatus', to='app.ShipStatus')),
            ],
        ),
    ]

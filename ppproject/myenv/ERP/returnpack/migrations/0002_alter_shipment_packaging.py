# Generated by Django 5.0.6 on 2024-06-06 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='packaging',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shipment', to='returnpack.packaging'),
        ),
    ]

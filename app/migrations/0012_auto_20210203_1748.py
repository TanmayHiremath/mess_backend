# Generated by Django 3.0.6 on 2021-02-03 12:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210203_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='data',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(null=True), size=5), size=31),
        ),
    ]
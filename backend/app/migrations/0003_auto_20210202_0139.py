# Generated by Django 3.0.6 on 2021-02-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210202_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='roll_number',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.0.6 on 2021-02-02 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210203_0251'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='month',
            unique_together={('roll_number', 'month')},
        ),
    ]

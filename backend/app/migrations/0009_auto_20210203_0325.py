# Generated by Django 3.0.6 on 2021-02-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210203_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True),
        ),
    ]

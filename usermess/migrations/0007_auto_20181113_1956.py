# Generated by Django 2.0.9 on 2018-11-13 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usermess', '0006_auto_20181113_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponsbought',
            name='boughtTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 14, 26, 0, 499278, tzinfo=utc)),
        ),
    ]

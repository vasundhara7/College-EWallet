# Generated by Django 2.0.9 on 2018-12-10 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20181118_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='student_id',
            field=models.CharField(default=0, max_length=12, validators=[django.core.validators.RegexValidator(code='invalid_cell', message='Enter a valid student id', regex='^[S]{1}[0-9]{11}$')]),
            preserve_default=False,
        ),
    ]

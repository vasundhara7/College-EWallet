# Generated by Django 2.0.9 on 2018-12-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_profile_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card_id',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

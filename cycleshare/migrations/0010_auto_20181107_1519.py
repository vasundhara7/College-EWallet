# Generated by Django 2.1.2 on 2018-11-07 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycleshare', '0009_auto_20181107_1425'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='available',
            new_name='availability',
        ),
    ]
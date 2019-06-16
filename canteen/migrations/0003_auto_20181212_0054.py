# Generated by Django 2.0.9 on 2018-12-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0002_card_pay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Studentid',
            new_name='PayId',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Studentid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Studentname',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Studentname',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default='hem1', max_length=150),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.CharField(default='hem1', max_length=150),
        ),
    ]
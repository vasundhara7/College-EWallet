# Generated by Django 2.0.9 on 2018-12-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_pay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flag', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 2.0.9 on 2018-11-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentid', models.IntegerField()),
                ('Studentname', models.CharField(max_length=100)),
                ('Itemname', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField(null=True)),
                ('OrderTime', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentid', models.IntegerField()),
                ('Studentname', models.CharField(max_length=100)),
                ('Amount', models.IntegerField()),
                ('PayTime', models.DateTimeField(blank=True)),
            ],
        ),
    ]

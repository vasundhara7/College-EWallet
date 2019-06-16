# Generated by Django 2.1.2 on 2018-11-14 17:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(blank=True, choices=[('', 'Select your year of study'), (1, 'Undergraduate 1'), (2, 'Undergraduate 2'), (3, 'Undergraduate 3'), (4, 'Undergraduate 4')], null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[('', 'Type of account'), (1, 'Student'), (2, 'Vendor')], null=True)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_cell', message='Enter a valid phone number', regex='^[1-9]{1}[0-9]{9}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

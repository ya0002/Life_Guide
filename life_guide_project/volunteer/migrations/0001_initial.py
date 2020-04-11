# Generated by Django 3.0.4 on 2020-04-11 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('Vol_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
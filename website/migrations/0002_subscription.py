# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial_number_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=15)),
                ('telegram', models.CharField(max_length=50)),
                ('email_confirmed', models.DateField()),
                ('phone_confirmed', models.DateField()),
                ('cancelled', models.DateField()),
                ('last_notify', models.DateField()),
                ('number', models.ForeignKey(to='website.Number')),
            ],
        ),
    ]

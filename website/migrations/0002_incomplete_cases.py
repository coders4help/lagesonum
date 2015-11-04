# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, timedelta
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial_number_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='appointment',
            field=models.DateField(verbose_name='appointment', blank=True, null=True, db_index=True),
        ),
        migrations.AddField(
            model_name='number',
            name='incomplete',
            field=models.BooleanField(verbose_name='incomplete registration', db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='number',
            name='number',
            field=models.CharField(unique=True, verbose_name='number', max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='number',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='number',
            name='fingerprint',
        ),
        migrations.AddField(
            model_name='place',
            name='validation_msg',
            field=models.CharField(verbose_name='pattern message', max_length=256, default='Invalid data %(data).'),
        ),
        migrations.AddField(
            model_name='place',
            name='per_day_incomplete',
            field=models.PositiveIntegerField(default=300, verbose_name='incomplete cases per day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='per_day_missed',
            field=models.PositiveIntegerField(default=100, verbose_name='missed appointments per day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='release_date',
            field=models.DateField(default=date.today() + timedelta(days=1), verbose_name='release date'),
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='dayoff', db_index=True)),
                ('location', models.ForeignKey(to='website.Place')),
            ],
            options={
                'verbose_name': 'holiday',
                'verbose_name_plural': 'holidays',
            },
        ),
    ]

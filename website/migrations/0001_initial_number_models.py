# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(verbose_name='number', max_length=30)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('fingerprint', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'number',
                'verbose_name_plural': 'numbers',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='place', unique=True, max_length=20)),
                ('validation', models.CharField(verbose_name='pattern', max_length=256)),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
        ),
        migrations.AddField(
            model_name='number',
            name='location',
            field=models.ForeignKey(to='website.Place', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='number',
            name='user',
            field=models.ForeignKey(null=True, related_name='+', to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterUniqueTogether(
            name='number',
            unique_together=set([('number', 'fingerprint')]),
        ),
    ]

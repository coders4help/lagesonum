# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20151025_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cancelled',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='last_notify',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='telegram',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]

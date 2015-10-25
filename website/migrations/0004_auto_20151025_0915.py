# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20151025_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.CharField(null=True, max_length=70, default=None),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(null=True, max_length=15, default=None),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='telegram',
            field=models.CharField(null=True, max_length=50, default=None),
        ),
    ]

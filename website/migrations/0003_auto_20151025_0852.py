# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='number',
            field=models.CharField(max_length=64),
        ),
    ]

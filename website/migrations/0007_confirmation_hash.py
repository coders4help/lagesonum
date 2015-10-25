# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20151025_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='confirmation_hash',
            field=models.SlugField(null=True, blank=True, default=None),
        ),
    ]

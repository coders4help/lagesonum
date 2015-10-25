# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20151025_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='telegram_confirmed',
            field=models.DateField(null=True),
        ),
    ]

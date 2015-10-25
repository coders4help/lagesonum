# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20151025_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cancelled',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email_confirmed',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='last_notify',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone_confirmed',
            field=models.DateField(null=True),
        ),
    ]

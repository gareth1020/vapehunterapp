# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20151209_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='eliquid',
            name='score',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
        ),
    ]

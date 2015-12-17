# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20151117_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='eliquid',
            name='site',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]

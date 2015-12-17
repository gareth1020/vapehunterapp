# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20151208_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='altphone',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='phone',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
    ]

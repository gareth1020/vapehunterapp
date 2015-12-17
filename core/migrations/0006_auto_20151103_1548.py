# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_eliquid_bottlesize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrengths',
            field=models.CommaSeparatedIntegerField(max_length=40, null=True, blank=True),
        ),
    ]

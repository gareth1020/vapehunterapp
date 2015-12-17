# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151103_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrengths',
            field=models.ManyToManyField(to='core.Nicstr', null=True, blank=True),
        ),
    ]

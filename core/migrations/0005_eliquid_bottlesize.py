# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151029_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='eliquid',
            name='bottlesize',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'5ml'), (1, b'10ml'), (2, b'15ml'), (3, b'30ml'), (4, b'60ml'), (5, b'120ml')]),
        ),
    ]

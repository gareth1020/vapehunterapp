# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_nicstr_nicstrengths'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliquid',
            name='pgratio',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='vgratio',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

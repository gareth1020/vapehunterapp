# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrengths',
            field=models.TextField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='pgratio',
            field=models.TextField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='vgratio',
            field=models.TextField(max_length=2, null=True, blank=True),
        ),
    ]

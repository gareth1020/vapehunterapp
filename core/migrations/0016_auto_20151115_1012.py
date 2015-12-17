# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20151111_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='city',
            field=models.TextField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='state',
            field=models.TextField(max_length=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='website',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151115_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='eliquid',
            name='search_var',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]

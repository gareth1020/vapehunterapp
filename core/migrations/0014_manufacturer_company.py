# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20151111_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='Company',
            field=models.CharField(default=12345, max_length=50),
            preserve_default=False,
        ),
    ]

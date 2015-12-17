# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20151208_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='phone',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
    ]

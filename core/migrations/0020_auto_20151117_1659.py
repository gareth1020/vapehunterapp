# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20151117_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enduser',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='enduser',
            name='birthday',
            field=models.CharField(max_length=100),
        ),
    ]

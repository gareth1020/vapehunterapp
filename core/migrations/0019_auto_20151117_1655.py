# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_enduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enduser',
            old_name='user',
            new_name='username',
        ),
    ]

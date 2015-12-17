# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_eliquid_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eliquid',
            old_name='site',
            new_name='page',
        ),
    ]

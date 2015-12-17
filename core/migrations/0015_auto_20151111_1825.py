# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_manufacturer_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='Company',
            new_name='company',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='account',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

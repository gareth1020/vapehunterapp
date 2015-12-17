# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20151209_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='altemail',
            new_name='alt_email',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='altphone',
            new_name='alt_phone',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='contactname',
            new_name='contact_name',
        ),
    ]

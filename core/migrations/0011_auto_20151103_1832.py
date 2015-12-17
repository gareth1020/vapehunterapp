# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151103_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eliquid',
            name='nicstrengths',
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrengths',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(0, b'1.5 mg/ml'), (1, b'3 mg/ml'), (2, b'6 mg/ml'), (3, b'12 mg/ml'), (4, b'18 mg/ml'), (5, b'24 mg/ml')]),
        ),
        migrations.DeleteModel(
            name='Nicstr',
        ),
    ]

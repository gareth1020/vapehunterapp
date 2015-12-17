# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20151208_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrength1',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'9', b'9 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrength2',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'9', b'9 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrength3',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'9', b'9 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrength4',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'9', b'9 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrength5',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'9', b'9 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrength6',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'9', b'9 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
    ]

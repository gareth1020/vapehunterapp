# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20151208_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='altemail',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='altphone',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

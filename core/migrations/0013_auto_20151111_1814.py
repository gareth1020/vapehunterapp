# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20151110_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eliquid',
            name='company',
        ),
        migrations.AddField(
            model_name='eliquid',
            name='manufacturer',
            field=models.ForeignKey(default=12345, to='core.Manufacturer'),
            preserve_default=False,
        ),
    ]

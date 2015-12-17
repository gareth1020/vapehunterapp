# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151103_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nicstr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eliquid',
            name='nicstrengths',
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrengths',
            field=models.ManyToManyField(to='core.Nicstr'),
        ),
    ]

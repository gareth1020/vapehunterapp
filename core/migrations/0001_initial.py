# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eliquid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('company', models.TextField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('flavor1', models.TextField(max_length=20)),
                ('flavor2', models.TextField(max_length=20, null=True, blank=True)),
                ('flavor3', models.TextField(max_length=20, null=True, blank=True)),
                ('flavor4', models.TextField(max_length=20, null=True, blank=True)),
                ('flavor5', models.TextField(max_length=20, null=True, blank=True)),
                ('pgratio', models.TextField(max_length=2)),
                ('vgratio', models.TextField(max_length=2)),
                ('nicstrengths', models.TextField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

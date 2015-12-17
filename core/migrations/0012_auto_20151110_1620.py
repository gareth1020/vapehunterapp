# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20151103_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eliquid',
            name='bottlesize',
        ),
        migrations.RemoveField(
            model_name='eliquid',
            name='nicstrengths',
        ),
        migrations.AddField(
            model_name='eliquid',
            name='bottlesize1',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'5', b'5ml'), (b'10', b'10ml'), (b'15', b'15ml'), (b'20', b'20ml'), (b'30', b'30ml'), (b'60', b'60ml'), (b'120', b'120ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='bottlesize2',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'5', b'5ml'), (b'10', b'10ml'), (b'15', b'15ml'), (b'20', b'20ml'), (b'30', b'30ml'), (b'60', b'60ml'), (b'120', b'120ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='bottlesize3',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'5', b'5ml'), (b'10', b'10ml'), (b'15', b'15ml'), (b'20', b'20ml'), (b'30', b'30ml'), (b'60', b'60ml'), (b'120', b'120ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='bottlesize4',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'5', b'5ml'), (b'10', b'10ml'), (b'15', b'15ml'), (b'20', b'20ml'), (b'30', b'30ml'), (b'60', b'60ml'), (b'120', b'120ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='bottlesize5',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'5', b'5ml'), (b'10', b'10ml'), (b'15', b'15ml'), (b'20', b'20ml'), (b'30', b'30ml'), (b'60', b'60ml'), (b'120', b'120ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrength1',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrength2',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrength3',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrength4',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrength5',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AddField(
            model_name='eliquid',
            name='nicstrength6',
            field=models.CharField(blank=True, max_length=13, null=True, choices=[(b'0', b'0 mg/ml'), (b'1.5', b'1.5 mg/ml'), (b'3', b'3 mg/ml'), (b'6', b'6 mg/ml'), (b'12', b'12 mg/ml'), (b'18', b'18 mg/ml'), (b'24', b'24 mg/ml')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor1',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Cucumber', b'Cucumber'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Honey', b'Honey'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Pralines', b'Pralines'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor2',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Cucumber', b'Cucumber'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Honey', b'Honey'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Pralines', b'Pralines'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor3',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Cucumber', b'Cucumber'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Honey', b'Honey'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Pralines', b'Pralines'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor4',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Cucumber', b'Cucumber'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Honey', b'Honey'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Pralines', b'Pralines'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor5',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Cucumber', b'Cucumber'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Honey', b'Honey'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Pralines', b'Pralines'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee')]),
        ),
    ]

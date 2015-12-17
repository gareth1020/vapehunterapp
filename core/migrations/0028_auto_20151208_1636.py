# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20151207_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='contactname',
            field=models.TextField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='email',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='phone',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor1',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Bavarian Cream', b'Bavarian Cream'), (b'Cantaloupe', b'Cantaloupe'), (b'Caramel', b'Caramel'), (b'Cream', b'Cream'), (b'Cucumber', b'Cucumber'), (b'Custard', b'Custard'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Graham', b'Graham'), (b'Guava', b'Guava'), (b'Honey', b'Honey'), (b'Honeydew', b'Honeydew'), (b'Mango', b'Mango'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Nuts', b'Nuts'), (b'Peanunt Butter', b'Peanut Butter'), (b'Pralines', b'Pralines'), (b'Strawberry', b'Strawberry'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee'), (b'Vanilla', b'Vanilla')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor2',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Bavarian Cream', b'Bavarian Cream'), (b'Cantaloupe', b'Cantaloupe'), (b'Caramel', b'Caramel'), (b'Cream', b'Cream'), (b'Cucumber', b'Cucumber'), (b'Custard', b'Custard'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Graham', b'Graham'), (b'Guava', b'Guava'), (b'Honey', b'Honey'), (b'Honeydew', b'Honeydew'), (b'Mango', b'Mango'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Nuts', b'Nuts'), (b'Peanunt Butter', b'Peanut Butter'), (b'Pralines', b'Pralines'), (b'Strawberry', b'Strawberry'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee'), (b'Vanilla', b'Vanilla')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor3',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Bavarian Cream', b'Bavarian Cream'), (b'Cantaloupe', b'Cantaloupe'), (b'Caramel', b'Caramel'), (b'Cream', b'Cream'), (b'Cucumber', b'Cucumber'), (b'Custard', b'Custard'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Graham', b'Graham'), (b'Guava', b'Guava'), (b'Honey', b'Honey'), (b'Honeydew', b'Honeydew'), (b'Mango', b'Mango'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Nuts', b'Nuts'), (b'Peanunt Butter', b'Peanut Butter'), (b'Pralines', b'Pralines'), (b'Strawberry', b'Strawberry'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee'), (b'Vanilla', b'Vanilla')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor4',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Bavarian Cream', b'Bavarian Cream'), (b'Cantaloupe', b'Cantaloupe'), (b'Caramel', b'Caramel'), (b'Cream', b'Cream'), (b'Cucumber', b'Cucumber'), (b'Custard', b'Custard'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Graham', b'Graham'), (b'Guava', b'Guava'), (b'Honey', b'Honey'), (b'Honeydew', b'Honeydew'), (b'Mango', b'Mango'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Nuts', b'Nuts'), (b'Peanunt Butter', b'Peanut Butter'), (b'Pralines', b'Pralines'), (b'Strawberry', b'Strawberry'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee'), (b'Vanilla', b'Vanilla')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor5',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Apple', b'Apple'), (b'Apricot', b'Apricot'), (b'Banana', b'Banana'), (b'Bavarian Cream', b'Bavarian Cream'), (b'Cantaloupe', b'Cantaloupe'), (b'Caramel', b'Caramel'), (b'Cream', b'Cream'), (b'Cucumber', b'Cucumber'), (b'Custard', b'Custard'), (b'Dark Chocolate', b'Dark Chocolate'), (b'Fig', b'Fig'), (b'Graham', b'Graham'), (b'Guava', b'Guava'), (b'Honey', b'Honey'), (b'Honeydew', b'Honeydew'), (b'Mango', b'Mango'), (b'Maple', b'Maple'), (b'Menthol', b'Menthol'), (b'Nuts', b'Nuts'), (b'Peanunt Butter', b'Peanut Butter'), (b'Pralines', b'Pralines'), (b'Strawberry', b'Strawberry'), (b'Tobacco', b'Tobacco'), (b'Toffee', b'Toffee'), (b'Vanilla', b'Vanilla')]),
        ),
    ]

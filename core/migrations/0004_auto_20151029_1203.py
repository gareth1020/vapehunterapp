# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151028_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliquid',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='description',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor1',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Amaretto'), (1, b'Anise'), (2, b'Apple Pie'), (3, b'Apricot'), (4, b'Bacon'), (5, b'Banana'), (6, b'Banana Split'), (7, b'Blackberry'), (8, b'Blue Raspberry Cotton Candy'), (9, b'Blueberry Cinnamon Crumble'), (10, b'Blueberry'), (11, b'Blueberry Pomegranate'), (12, b'Bold Tobacco'), (13, b'Boston Cream Pie'), (14, b'Bubble Gum Flavor'), (15, b'Cake Batter'), (16, b'Cantaloupe'), (17, b'Cappuccino'), (18, b'Caramel'), (19, b'Chai Tea'), (20, b'Cherry Cola'), (21, b'Chocolate Caramel Nut'), (22, b'Chocolate Coconut Almond'), (23, b'Chocolate Fudge Brownie'), (24, b'Chocolate Glazed Doughnut'), (25, b'Chocolate Raspberry'), (26, b'Cinnamon Coffee Cake'), (27, b'Cinnamon Danish Swirl'), (28, b'Coconut'), (29, b'Cola'), (30, b'Concord Grape'), (31, b'Cool Mint'), (32, b'Cranberry'), (33, b'Creamy Yogurt'), (34, b'Cucumber'), (35, b'Double Apple')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor2',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Amaretto'), (1, b'Anise'), (2, b'Apple Pie'), (3, b'Apricot'), (4, b'Bacon'), (5, b'Banana'), (6, b'Banana Split'), (7, b'Blackberry'), (8, b'Blue Raspberry Cotton Candy'), (9, b'Blueberry Cinnamon Crumble'), (10, b'Blueberry'), (11, b'Blueberry Pomegranate'), (12, b'Bold Tobacco'), (13, b'Boston Cream Pie'), (14, b'Bubble Gum Flavor'), (15, b'Cake Batter'), (16, b'Cantaloupe'), (17, b'Cappuccino'), (18, b'Caramel'), (19, b'Chai Tea'), (20, b'Cherry Cola'), (21, b'Chocolate Caramel Nut'), (22, b'Chocolate Coconut Almond'), (23, b'Chocolate Fudge Brownie'), (24, b'Chocolate Glazed Doughnut'), (25, b'Chocolate Raspberry'), (26, b'Cinnamon Coffee Cake'), (27, b'Cinnamon Danish Swirl'), (28, b'Coconut'), (29, b'Cola'), (30, b'Concord Grape'), (31, b'Cool Mint'), (32, b'Cranberry'), (33, b'Creamy Yogurt'), (34, b'Cucumber'), (35, b'Double Apple')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor3',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Amaretto'), (1, b'Anise'), (2, b'Apple Pie'), (3, b'Apricot'), (4, b'Bacon'), (5, b'Banana'), (6, b'Banana Split'), (7, b'Blackberry'), (8, b'Blue Raspberry Cotton Candy'), (9, b'Blueberry Cinnamon Crumble'), (10, b'Blueberry'), (11, b'Blueberry Pomegranate'), (12, b'Bold Tobacco'), (13, b'Boston Cream Pie'), (14, b'Bubble Gum Flavor'), (15, b'Cake Batter'), (16, b'Cantaloupe'), (17, b'Cappuccino'), (18, b'Caramel'), (19, b'Chai Tea'), (20, b'Cherry Cola'), (21, b'Chocolate Caramel Nut'), (22, b'Chocolate Coconut Almond'), (23, b'Chocolate Fudge Brownie'), (24, b'Chocolate Glazed Doughnut'), (25, b'Chocolate Raspberry'), (26, b'Cinnamon Coffee Cake'), (27, b'Cinnamon Danish Swirl'), (28, b'Coconut'), (29, b'Cola'), (30, b'Concord Grape'), (31, b'Cool Mint'), (32, b'Cranberry'), (33, b'Creamy Yogurt'), (34, b'Cucumber'), (35, b'Double Apple')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor4',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Amaretto'), (1, b'Anise'), (2, b'Apple Pie'), (3, b'Apricot'), (4, b'Bacon'), (5, b'Banana'), (6, b'Banana Split'), (7, b'Blackberry'), (8, b'Blue Raspberry Cotton Candy'), (9, b'Blueberry Cinnamon Crumble'), (10, b'Blueberry'), (11, b'Blueberry Pomegranate'), (12, b'Bold Tobacco'), (13, b'Boston Cream Pie'), (14, b'Bubble Gum Flavor'), (15, b'Cake Batter'), (16, b'Cantaloupe'), (17, b'Cappuccino'), (18, b'Caramel'), (19, b'Chai Tea'), (20, b'Cherry Cola'), (21, b'Chocolate Caramel Nut'), (22, b'Chocolate Coconut Almond'), (23, b'Chocolate Fudge Brownie'), (24, b'Chocolate Glazed Doughnut'), (25, b'Chocolate Raspberry'), (26, b'Cinnamon Coffee Cake'), (27, b'Cinnamon Danish Swirl'), (28, b'Coconut'), (29, b'Cola'), (30, b'Concord Grape'), (31, b'Cool Mint'), (32, b'Cranberry'), (33, b'Creamy Yogurt'), (34, b'Cucumber'), (35, b'Double Apple')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='flavor5',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Amaretto'), (1, b'Anise'), (2, b'Apple Pie'), (3, b'Apricot'), (4, b'Bacon'), (5, b'Banana'), (6, b'Banana Split'), (7, b'Blackberry'), (8, b'Blue Raspberry Cotton Candy'), (9, b'Blueberry Cinnamon Crumble'), (10, b'Blueberry'), (11, b'Blueberry Pomegranate'), (12, b'Bold Tobacco'), (13, b'Boston Cream Pie'), (14, b'Bubble Gum Flavor'), (15, b'Cake Batter'), (16, b'Cantaloupe'), (17, b'Cappuccino'), (18, b'Caramel'), (19, b'Chai Tea'), (20, b'Cherry Cola'), (21, b'Chocolate Caramel Nut'), (22, b'Chocolate Coconut Almond'), (23, b'Chocolate Fudge Brownie'), (24, b'Chocolate Glazed Doughnut'), (25, b'Chocolate Raspberry'), (26, b'Cinnamon Coffee Cake'), (27, b'Cinnamon Danish Swirl'), (28, b'Coconut'), (29, b'Cola'), (30, b'Concord Grape'), (31, b'Cool Mint'), (32, b'Cranberry'), (33, b'Creamy Yogurt'), (34, b'Cucumber'), (35, b'Double Apple')]),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='nicstrengths',
            field=models.IntegerField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='pgratio',
            field=models.IntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eliquid',
            name='vgratio',
            field=models.IntegerField(max_length=3, null=True, blank=True),
        ),
    ]

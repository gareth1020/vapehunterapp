from __future__ import division
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg



RATING_CHOICES = (
    (0, 'None'),
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
    )

FLAVOR_CHOICES = (
	('Apple', 'Apple'),
	('Apricot', 'Apricot'),
	('Banana', 'Banana'),
	('Bavarian Cream', 'Bavarian Cream'),
	('Bergamot', 'Bergamot'),
	('Berries', 'Berries'),
	('Berry', 'Berry'),
	('Blueberry', 'Blueberry'),
	('Cinnamon', 'Cinnamon'),
	('Cantaloupe', 'Cantaloupe'),
	('Caramel', 'Caramel'),
	('Cereal', 'Cereal'),
	('Chocolate', 'Chocolate'),
	('Cobbler', 'Cobbler'),
	('Coconut', 'Coconut'),
	('Cookie', 'Cookie'),
	('Cooling', 'Cooling'),
	('Cream', 'Cream'),
	('Creamy', 'Creamy'),
	('Crumble', 'Crumble'),
	('Cucumber', 'Cucumber'),
	('Custard', 'Custard'),
	('Dark Chocolate', 'Dark Chocolate'),
	('Dessert', 'Dessert'),
	('Fig', 'Fig'),
	('Floral', 'Floral'),
	('Fruit', 'Fruit'),
	('Fruity', 'Fruity'),
	('Graham', 'Graham'),
	('Graham Cracker', 'Graham Cracker'),
	('Guava', 'Guava'),
	('Gummy', 'Gummy'),
	('Hibiscus', 'Hibiscus'),
	('Honey', 'Honey'),
	('Honeydew', 'Honeydew'),
	('Honeysuckle', 'Honeysuckle'),
	('Ice Cream', 'Ice Cream'),
	('Juicy', 'Juicy'),
	('Kiwi', 'Kiwi'),
	('Lime', 'Lime'),
	('Mango', 'Mango'),
	('Maple', 'Maple'),
	('Marshmallow', 'Marshmallow'),
	('Menthol', 'Menthol'),
	('Milky', 'Milky'),
	('Nuts', 'Nuts'),
	('Orange', 'Orange'),
	('Parfait', 'Parfait'),
	('Pastry', 'Pastry'),
	('Peach', 'Peach'),
	('Pear', 'Pear'),
	('Peanunt Butter', 'Peanut Butter'),
	('Pineapple', 'Pineapple'),
	('Popsicle', 'Popsicle'),
	('Pralines', 'Pralines'),
	('Strawberry', 'Strawberry'),
	('Taffy', 'Taffy'),
	('Tea', 'Tea'),
	('Tobacco', 'Tobacco'),
	('Toffee', 'Toffee'),
	('Vanilla', 'Vanilla'),
	('Waffle Cone', 'Waffle Cone'),
	('Watermelon', 'Watermelon'),
	)

BOTTLE_SIZES = (
	('5', '5ml'),
	('10', '10ml'),
	('15', '15ml'),
	('20', '20ml'),
	('30', '30ml'),
	('60', '60ml'),
	('120', '120ml'),
	)

NIC_STR = (
	('0', '0 mg/ml'),
	('1.5', '1.5 mg/ml'),
	('3', '3 mg/ml'),
	('6', '6 mg/ml'),
	('9', '9 mg/ml'),
	('12', '12 mg/ml'),
	('18', '18 mg/ml'),
	('24', '24 mg/ml'),
	)

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return unicode (self.user)

class Manufacturer(models.Model):
	company = models.CharField(max_length=50)
	account = models.IntegerField(null=True, blank=True)
	email = models.CharField(max_length=150, null=True, blank=True)
	alt_email = models.CharField(max_length=150, null=True, blank=True)
	contact_name = models.TextField(max_length=30, null=True, blank=True)
	phone = models.CharField(max_length=12, null=True, blank=True)
	alt_phone = models.CharField(max_length=12, null=True, blank=True)
	city = models.TextField(max_length=30, null=True, blank=True)
	state = models.TextField(max_length=2, null=True, blank=True)
	website = models.CharField(max_length=150, null=True, blank=True)

	def __unicode__(self):
         return self.company

class Eliquid(models.Model):
	title = models.CharField(max_length=50)
	manufacturer = models.ForeignKey(Manufacturer)
	description = models.CharField(max_length=400, null=True, blank=True)
	flavor1 = models.CharField(max_length=30, choices=FLAVOR_CHOICES, null=True, blank=True)
	flavor2 = models.CharField(max_length=30, choices=FLAVOR_CHOICES, null=True, blank=True)
	flavor3 = models.CharField(max_length=30, choices=FLAVOR_CHOICES, null=True, blank=True)
	flavor4 = models.CharField(max_length=30, choices=FLAVOR_CHOICES, null=True, blank=True)
	flavor5 = models.CharField(max_length=30, choices=FLAVOR_CHOICES, null=True, blank=True)
	pgratio = models.IntegerField(null=True, blank=True)
	vgratio = models.IntegerField(null=True, blank=True)
	nicstrength1 = models.CharField(max_length=13, choices=NIC_STR, null=True, blank=True)
	nicstrength2 = models.CharField(max_length=13, choices=NIC_STR, null=True, blank=True)
	nicstrength3 = models.CharField(max_length=13, choices=NIC_STR, null=True, blank=True)
	nicstrength4 = models.CharField(max_length=13, choices=NIC_STR, null=True, blank=True)
	nicstrength5 = models.CharField(max_length=13, choices=NIC_STR, null=True, blank=True)
	nicstrength6 = models.CharField(max_length=13, choices=NIC_STR, null=True, blank=True)
	bottlesize1 = models.CharField(max_length=100, choices=BOTTLE_SIZES, null=True, blank=True)
	bottlesize2 = models.CharField(max_length=100, choices=BOTTLE_SIZES, null=True, blank=True)
	bottlesize3 = models.CharField(max_length=100, choices=BOTTLE_SIZES, null=True, blank=True)
	bottlesize4 = models.CharField(max_length=100, choices=BOTTLE_SIZES, null=True, blank=True)
	bottlesize5 = models.CharField(max_length=100, choices=BOTTLE_SIZES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	search_var = models.CharField(max_length=500, null=True, blank=True)
	page = models.CharField(max_length=150, null=True, blank=True)
	score = models.DecimalField(default=0, max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="eliquids_list", args=[self.id])

	def get_average_rating(self):
		average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
		if average == None:
			return average
		else: 
			float(average)
			rounded_average = ((int)(average * 10) / 10.0)
			return rounded_average

	def get_reviews(self):
		return self.review_set.all()

class Review(models.Model):
	eliquid = models.ForeignKey(Eliquid)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

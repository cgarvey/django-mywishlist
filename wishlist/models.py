from django.db import models

#pylint: disable-msg=W0232
class Category( models.Model ):
	created_date_time = models.DateTimeField( auto_now_add=True )
	modified_date_time = models.DateTimeField( auto_now=True )

	is_active = models.BooleanField( default=True )
	name = models.CharField( max_length=64 )
	sort_order = models.IntegerField( default=0 )

	class Meta:
		verbose_name_plural = 'categories'

	# Standard
	def __unicode__( self ):
		return self.name
	def __str__( self ):
		return self.name
	@staticmethod
	def __abbrev__(): return "CAT"
	# Getters
	# Utils

class Item( models.Model ):
	created_date_time = models.DateTimeField( auto_now_add=True )
	modified_date_time = models.DateTimeField( auto_now=True )

	category = models.ForeignKey( "Category", related_name="itm_category_cat" )
	is_booked = models.BooleanField( default=True )
	image_slug = models.CharField( max_length=16, blank=True, null=True )
	name = models.CharField( max_length=64 )
	price = models.DecimalField( decimal_places=2, max_digits=10, blank=True, null=True )
	sort_order = models.IntegerField( default=0 )
	url = models.URLField( blank=True, null=True )

	# Standard
	def __unicode__( self ):
		return self.name
	def __str__( self ):
		return self.name
	@staticmethod
	def __abbrev__(): return "ITM"
	# Getters
	# Utils


## Django Admin
from django.contrib import admin
admin.site.register( Category )
admin.site.register( Item )

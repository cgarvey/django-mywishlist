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
	description = models.TextField( max_length=1024, blank=True, null=True )
	is_active = models.BooleanField( default=True )
	is_booked = models.BooleanField( default=True )
	image_slug = models.CharField( max_length=16, blank=True, null=True )
	image_url = models.URLField( blank=True, null=True )
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
	def preferred_image_url( self ):
		'''
		Get the image URL to use for this item's image. In order, item
		will attempt to use the uploaded image (slug), then the provided URL,
		and finally a random (theme-provided) one.
		'''
		import random

		if( self.image_slug ): return self.image_slug
		elif( self.image_url ): return self.image_url
		else: return "/static/wishlist/img/portfolio/%s.png" % random.choice( ["cake", "cabin", "circus", "game", "safe", "submarine"] )
	def url_domain( self ):
		'''
		Get the domain of the URL, if any
		'''
		from urlparse import urlparse

		if( self.url ):
			o = urlparse( self.url )
			if( o and o.netloc ):
				domain = o.netloc
				# Strip www.
				if( len( domain ) > 4 and domain[:4] == "www." ): domain = domain[4:]
				return domain
		return None

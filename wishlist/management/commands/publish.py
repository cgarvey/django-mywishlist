from django.core.management.base import BaseCommand

class Command(BaseCommand):
	def handle( self, **options ):
		from django.template.loader import render_to_string
		from wishlist.models import Item

		filename = "publish/index.html"

		print "Retrieving Items"
		ls_itm = Item.objects.filter( is_active=True ).order_by( "category__sort_order", "category__id", "sort_order" ).prefetch_related( "category" )
		if( ls_itm ):
			print "OK, have %d" % len( ls_itm )

			print "Sorting items"
			data = []
			last_category_id = 0
			if( ls_itm ):
				for itm in ls_itm:
					if( last_category_id != itm.category.id ):
						data.append( [] )
						last_category_id = itm.category.id
					arr = data[-1]
					arr.append( itm )

			print "Rendering template"
			html = render_to_string( "wishlist/index.html", { "data":data } )

			print "Writing to file (%s)" % filename
			f = open( filename, "w" )
			f.write( html )
			print "Done."

		else: print "OK (none)."

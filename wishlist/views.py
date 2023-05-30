from django.shortcuts import render

# Create your views here.
def index( request ):
	''' Default view (for visitors to the root URL) which presents login form, processes login form, or redirects
	to dashboard if already logged in'''

	from wishlist.models import Item

	data = []
	ls_items = Item.objects.filter( is_active=True ).order_by( "category__sort_order", "category__id", "sort_order" ).prefetch_related( "category" )

	last_category_id = 0
	if( ls_items ):
		for item in ls_items:
			if( last_category_id != item.category.id ):
				data.append( [] )
				last_category_id = item.category.id
			arr = data[-1]
			arr.append( item )

	return render( request, "wishlist/index.html", { "data":data } )

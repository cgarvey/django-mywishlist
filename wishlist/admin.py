## Django Admin
from django.contrib import admin

from wishlist.models import Item

#admin.site.register( Category )
#admin.site.register( Item )

class ItemAdmin( admin.ModelAdmin ) :
	list_display = ( "id", "name", "category", "sort_order", "price" )
	list_filter = ( "is_active", "category" )
	search_fields = ( 'name', )
	list_per_page = 30
admin.site.register( Item, ItemAdmin )

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^djadmin/', include(admin.site.urls)),

	# Root
	url( r'^$', 'wishlist.views.index' ),
)

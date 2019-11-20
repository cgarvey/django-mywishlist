from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from wishlist import views

urlpatterns = [
    url(r'^djadmin/', include(admin.site.urls)),

	# Root
	url( r'^$', views.index ),
]

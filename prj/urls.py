from django.urls import path
from django.contrib import admin

admin.autodiscover()

from wishlist import views

urlpatterns = [
	path('djadmin/', admin.site.urls),

	# Root
	path( '', views.index ),
]

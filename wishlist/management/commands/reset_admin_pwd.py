from django.core.management.base import BaseCommand

class Command(BaseCommand):
	def handle( self, **options ):
		from django.contrib.auth.models import User
		users = User.objects.all()
		for user in users:
			user.set_password('admin');
			user.save()

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'
	
	def add_arguments(self, parser):
		parser.add_argument('nombre', nargs='+', type=str)
	
	def handle(self, *args, **options):
		for elem in options['nombre']:
			self.stdout.write(elem)
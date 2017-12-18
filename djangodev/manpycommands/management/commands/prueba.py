from django.core.management.base import BaseCommand, CommandError

from django.core import management

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'
	
	def add_arguments(self, parser):
		parser.add_argument('nombre', nargs='+', type=str)
	
	def handle(self, *args, **options):

		management.call_command('migrate', 'contenttypes', '0001_initial')
		management.call_command('migrate', 'auth', '0001_initial')
		management.call_command('migrate', 'admin')
		management.call_command('migrate', 'contenttypes', '0002_remove_content_type_name')
		management.call_command('migrate', 'auth')
		management.call_command('migrate', 'sessions')
		management.call_command('migrate', 'manpycommands', '0001_proyecto')
		management.call_command('migrate', 'manpycommands', '0002_permisos')
		management.call_command(
			'createsuperuser',
			username='froylan',
			email='jmalaga@idom.com'
			)

		'''
		for elem in options['nombre']:
			self.stdout.write(elem)
		        import ipdb; ipdb.set_trace()
		'''

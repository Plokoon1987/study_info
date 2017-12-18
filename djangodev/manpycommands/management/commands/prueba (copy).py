from django.core.management.base import BaseCommand, CommandError

from django.core import management

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'
	
	def add_arguments(self, parser):
		parser.add_argument('nombre', nargs='+', type=str)
	
	def handle(self, *args, **options):
		from importlib import import_module
		
		from django.apps import apps
		
		from django.db import connections
		from django.db.migrations.executor import MigrationExecutor
		from django.utils.module_loading import module_has_submodule
		
		for app_config in apps.get_app_configs():
			if module_has_submodule(app_config.module, "management"):
				import_module('.management', app_config.name)
		
		# Get the database we're operating from
		connection = connections['default']
		# Hook for backends needing any database preparation
		connection.prepare_database()
		
		executor = MigrationExecutor(connection)
		
		targets = [
		('admin', '0002_logentry_remove_auto_add'), 		
		('auth','0008_alter_user_username_max_length'),
		('contenttypes', '0002_remove_content_type_name'),
		('sessions', '0001_initial')
		]
		
		plan = executor.migration_plan(targets)
		
		executor.migrate(targets, plan=plan)
		
		import ipdb; ipdb.set_trace()
		
		'''
		
		management.call_command('migrate', targets)
		
		
		management.call_command('migrate', 'auth')
		
		management.call_command('migrate', ['admin'])
		management.call_command('migrate', 'sessions')
		management.call_command('migrate', 'manpycommands', '0001_proyecto')
		management.call_command('migrate', 'manpycommands', '0002_permisos')
		'''
		for elem in options['nombre']:
			self.stdout.write(elem)
		#        import ipdb; ipdb.set_trace()

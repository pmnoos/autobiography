from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Reset demo user password to demo123'

    def handle(self, *args, **options):
        try:
            # Get the demo user
            user = User.objects.get(username='demo')
            
            # Reset password to demo123
            user.password = make_password('demo123')
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully reset password for user "{user.username}" to "demo123"'
                )
            )
            
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    'Demo user does not exist. Run "python manage.py setup_default_user" first.'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {e}')
            ) 
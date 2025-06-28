from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Set up default login credentials for new users'

    def handle(self, *args, **options):
        # Default credentials
        default_username = 'demo'
        default_password = 'demo123'
        default_email = 'demo@example.com'
        
        # Check if user already exists
        if User.objects.filter(username=default_username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f'User "{default_username}" already exists. Skipping creation.'
                )
            )
            return
        
        # Create default user
        user = User.objects.create(
            username=default_username,
            email=default_email,
            password=make_password(default_password),
            is_staff=True,
            is_superuser=True
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Default user created successfully!\n'
                f'Username: {default_username}\n'
                f'Password: {default_password}\n'
                f'Email: {default_email}\n\n'
                f'⚠️  IMPORTANT: Change these credentials immediately after first login!'
            )
        ) 
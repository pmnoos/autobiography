from django.conf import settings

def template_settings(request):
    """
    Context processor to make template customization settings available in all templates
    """
    return {
        'COMMERCIAL_MODE': getattr(settings, 'COMMERCIAL_MODE', True),
        'SITE_TITLE': getattr(settings, 'SITE_TITLE', 'My Life Story'),
        'SITE_SUBTITLE': getattr(settings, 'SITE_SUBTITLE', 'The Story of My Life'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'Welcome to my personal autobiography'),
        'AUTHOR_NAME': getattr(settings, 'AUTHOR_NAME', 'Your Name'),
        'AUTHOR_SIGNATURE': getattr(settings, 'AUTHOR_SIGNATURE', 'Thanks for reading my story, Your Name'),
    } 
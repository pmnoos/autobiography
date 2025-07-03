from django.conf import settings

def template_settings(request):
    """Add template settings context to all templates"""
    return {
        'SITE_TITLE': 'LifeStory Platform',
        'SITE_SUBTITLE': 'Professional Life Story Creation',
        'SITE_DESCRIPTION': 'Create, preserve, and share your life story with our professional autobiography platform.',
        'AUTHOR_SIGNATURE': 'Your Story, Beautifully Told',
    }

def translations(request):
    """Add translation context to all templates"""
    return {
        'LANGUAGE_CODE': getattr(settings, 'LANGUAGE_CODE', 'en'),
        'LANGUAGES': getattr(settings, 'LANGUAGES', []),
    } 
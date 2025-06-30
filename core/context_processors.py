from django.conf import settings

def template_settings(request):
    """Add template settings context to all templates"""
    return {
        'SITE_TITLE': 'My Life Story',
        'SITE_SUBTITLE': 'My Personal Journey',
        'SITE_DESCRIPTION': 'A digital memoir of my life experiences, memories, and stories.',
        'AUTHOR_SIGNATURE': 'Written with love and memories',
    }

def translations(request):
    """Add translation context to all templates"""
    return {
        'LANGUAGE_CODE': getattr(settings, 'LANGUAGE_CODE', 'en'),
        'LANGUAGES': getattr(settings, 'LANGUAGES', []),
    } 
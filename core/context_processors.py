from django.conf import settings

def template_settings(request):
    """Add template settings context to all templates"""
    return {
        'SITE_TITLE': "Peter's Autobiography",
        'SITE_SUBTITLE': 'The Story of an Ordinary Man with an Extra-ordinary Life',
        'SITE_DESCRIPTION': 'A personal journey through life, love, and adventure.',
        'AUTHOR_SIGNATURE': 'Thanks for sticking around — you deserve a medal... or at least a cup of tea',
    }

def translations(request):
    """Add translation context to all templates"""
    return {
        'LANGUAGE_CODE': getattr(settings, 'LANGUAGE_CODE', 'en'),
        'LANGUAGES': getattr(settings, 'LANGUAGES', []),
    } 
from django.conf import settings

def template_settings(request):
    """
    Context processor to make template customization settings available in all templates
    """
    return {
        'COMMERCIAL_MODE': getattr(settings, 'COMMERCIAL_MODE', False),
        'SITE_TITLE': getattr(settings, 'SITE_TITLE', 'MyStory'),
        'SITE_SUBTITLE': getattr(settings, 'SITE_SUBTITLE', 'The Story of an Ordinary Man with an Extra-ordinary Life'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'Through the simplicity of my existence, I unearthed the profound truth that to love and to be loved is the greatest adventure of all...'),
        'AUTHOR_NAME': getattr(settings, 'AUTHOR_NAME', 'Peter'),
        'AUTHOR_SIGNATURE': getattr(settings, 'AUTHOR_SIGNATURE', 'Thanks for sticking around — you deserve a medal... or at least a cup of tea, Peter'),
    } 
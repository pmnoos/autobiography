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
    # Simple fallback translations
    translations_dict = {
        'en': {
            'home': 'Home',
            'getting_started': 'Getting Started',
            'new_chapter': 'New Chapter',
            'photo_gallery': 'Photo Gallery',
            'upload_images': 'Upload Images',
            'admin_panel': 'Admin Panel',
            'download_backup': 'Download Backup',
            'login': 'Login',
            'logout': 'Logout',
            'welcome': 'Welcome',
            'your_life_story': 'Your Life Story - Beautifully Told',
            'subtitle': 'Create, organize, and share your personal autobiography with chapters, photos, and memories. Turn your life experiences into a beautiful digital legacy.',
            'footer_quote': 'Every life is a story worth telling',
            'footer_signature': 'Personal Autobiography App',
        },
        'es': {
            'home': 'Inicio',
            'getting_started': 'Comenzar',
            'new_chapter': 'Nuevo Capítulo',
            'photo_gallery': 'Galería de Fotos',
            'upload_images': 'Subir Imágenes',
            'admin_panel': 'Panel de Admin',
            'download_backup': 'Descargar Respaldo',
            'login': 'Iniciar Sesión',
            'logout': 'Cerrar Sesión',
            'welcome': 'Bienvenido',
            'your_life_story': 'Tu Historia de Vida - Hermosamente Contada',
            'subtitle': 'Crea, organiza y comparte tu autobiografía personal con capítulos, fotos y recuerdos. Convierte tus experiencias de vida en un hermoso legado digital.',
            'footer_quote': 'Cada vida es una historia que vale la pena contar',
            'footer_signature': 'Aplicación de Autobiografía Personal',
        },
        'fr': {
            'home': 'Accueil',
            'getting_started': 'Commencer',
            'new_chapter': 'Nouveau Chapitre',
            'photo_gallery': 'Galerie Photos',
            'upload_images': 'Télécharger Images',
            'admin_panel': 'Panneau Admin',
            'download_backup': 'Télécharger Sauvegarde',
            'login': 'Se Connecter',
            'logout': 'Se Déconnecter',
            'welcome': 'Bienvenue',
            'your_life_story': 'Votre Histoire de Vie - Magnifiquement Racontee',
            'subtitle': 'Créez, organisez et partagez votre autobiographie personnelle avec des chapitres, des photos et des souvenirs. Transformez vos expériences de vie en un magnifique héritage numérique.',
            'footer_quote': 'Chaque vie est une histoire qui mérite d\'être racontée',
            'footer_signature': 'Application d\'Autobiographie Personnelle',
        }
    }
    
    # Get current language from session or default to 'en'
    current_language = request.session.get('django_language', 'en')
    
    # Create a translation function that uses the current language
    def t(key):
        return translations_dict.get(current_language, translations_dict['en']).get(key, key)
    
    return {
        't': t,
        'current_language': current_language,
        'available_languages': list(translations_dict.keys()),
    } 
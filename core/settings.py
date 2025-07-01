from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-r^c!!%=!yh&f7#4pdimu&e)v_kfc-8u201xl9rn=ay@a2+-#lc')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['*']  # For development and testing on Render

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chapters',
    'gallery',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #"whitenoise.middleware.WhiteNoiseMiddleware",  # Move this to position 2
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'  # Make sure this matches your actual project

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'core.context_processors.translations',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')  # Local fallback
    
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False  # Disable Django's built-in internationalization
USE_L10N = False  # Disable Django's built-in localization
USE_TZ = True

# Available languages (for our custom system)
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español'),
    ('fr', 'Français'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise configuration for Render (Updated for newer Django)
#STORAGES = {
 #   "staticfiles": {
  #      "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
   # },
#}

# Add this line to settings.py
3#TATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'silver',
    'plugins': 'link image media code',
    'toolbar': 'undo redo | bold italic | alignleft aligncenter alignright | link image code',
    'file_picker_callback': """
        function(callback, value, meta) {
            var input = document.createElement("input");
            input.setAttribute("type", "file");
            input.setAttribute("accept", "image/*");
            input.click();
            input.onchange = function() {
                var file = input.files[0];
                var reader = new FileReader();
                reader.onload = function(e) {
                    callback(e.target.result);
                };
                reader.readAsDataURL(file);
            };
        }
    """,
}

# Auth
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = "/login/"
LOGIN_REDIRECT_URL = "/"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

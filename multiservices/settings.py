import os
from pathlib import Path
from easy_thumbnails.conf import Settings as thumbnail_settings

SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')

BASE_DIR = Path(__file__).resolve().parent.parent

#import environ
#env = environ.Env()
#environ.Env.read_env()


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']

AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account.apps.AccountConfig',
    'Booking.apps.BookingConfig',
    'Cart.apps.CartConfig',
    'oauth2_provider',
    'easy_thumbnails',
    'image_cropping',  # Add 'image_cropping' to your installed apps
]

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line for serving static files efficiently
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.ApprovalMiddleware',
]


# Root URL configuration
ROOT_URLCONF = 'multiservices.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates'),  # Main templates directory
             os.path.join(BASE_DIR, 'Booking', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Cart.context_processors.cart',

            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'multiservices.wsgi.application'

import dj_database_url

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



#import dj_database_url

#DATABASES = {
 #   'default':  dj_database_url.parse(env('DATABASE_URL'))
  #   

   # }


# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Language and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = BASE_DIR / 'productionfiles'


# Custom authentication backends
AUTHENTICATION_BACKENDS = [
    'account.backends.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# OAuth2 Provider Settings
#OAUTH2_PROVIDER = {
 #   'SCOPES': {
  #      'read': 'Read scope',
   #     'write': 'Write scope',
    #    'groups': 'Access to your groups',
    #}
#}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# IMAGE CROPPING Configuration
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server address
EMAIL_PORT = 587  # SMTP server port
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = 'hads1kiki@gmail.com'  
EMAIL_HOST_PASSWORD = 'jxrt rxfv xrrh fono'  
EMAIL_SUBJECT_PREFIX = '[MyApp] '  
ADMIN_EMAIL = 'hads1kiki@gmail.com'  
DEFAULT_FROM_EMAIL = 'hads1kiki@gmail.com' 

# IMAGE CROPPING Configuration
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}
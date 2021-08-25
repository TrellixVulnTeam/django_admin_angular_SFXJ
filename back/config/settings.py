"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9k33l&d_@luy(4)vw$6$%sf(%3mzl4+3=62p4j*z=dy#&ln#m_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '127.0.0.1:8000', '[::1]', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    #para django-admin pluggin. Antes de 'django.contrib.admin',    
    #'admin_interface',        
    #'colorfield',
    #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    #habilitar el token
    'rest_framework.authtoken',
    #DRF
    'rest_framework',
    'corsheaders',    
    'apps.api',
    'apps.bases',    
    'apps.empresas',
    'apps.trabajadores',
    'apps.gdocumental',
    'apps.stock',     
    'apps.pgou', 
    'apps.catastro', 
    'apps.ibi', 
    'apps.solicitud', 
    #apps configuradas
    'nested_admin',
     #añadirmos la app swagger
    #'rest_framework_swagger',
]

#para django-admin pluggin
X_FRAME_OPTIONS='SAMEORIGIN' # only if django version >= 3.0

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#ROOT_URLCONF = 'api.urls'
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#WSGI_APPLICATION = 'api.wsgi.application'
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}

    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'apiadmin',
      'USER': 'javier',
      'PASSWORD': '2525_ap',
      'HOST': 'localhost',      
      'PORT': '5432'      
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-us'
#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
#TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/code/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/base/')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'    
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
DATE_INPUT_FORMATS = ( "%d/%m/%Y", )
DATETIME_INPUT_FORMATS = ( "%d/%m/%Y %H:%M", )

USE_THOUSAND_SEPARATOR = True

CORS_ORIGIN_WHITELIST = [
    ##direcciones de las que acepta recibir peticiones de post/get
    "http://localhost:8000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://localhost:3000",        
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    #"http://localhost:4200/login",    
]

#LOGIN
#LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/admin'
#LOGOUT_REDIRECT_URL = '/login/'
LOGOUT_REDIRECT_URL = '/admin/'


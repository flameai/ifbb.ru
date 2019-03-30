"""
Django settings for ifbb project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import os

if os.environ.get['PRODKEY']:
    PRODUCTION = True
else:
    PRODUCTION = False

DEBUG = not PRODUCTION
TEMPLATE_DEBUG = DEBUG

# ...








# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sc#b$opq@w9z6-i&mqke#y@omp9%3^(b_#*e)2@_8os!(1o@h('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =  ['localhost', '127.0.0.1', '[::1]','www2.ifbb.ru']


# Application definition

INSTALLED_APPS = [
    'suit_ckeditor',
    'suit',
    'suit_redactor',
    'mainapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ifbb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ifbb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases



if PRODUCTION:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/var/run/mysqld/mysqld.sock',
            'NAME': 'c6582_new3_ifbb_ru',
            'USER': 'c6582_new3_ifbb_ru',
            'PASSWORD': 'QuZxuFamgozus25',
        },
    }
   
  

else:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if PRODUCTION:
    STATIC_ROOT ='/home/c6582/www/static/'
    CKEDITOR_UPLOAD_PATH = 'C:/djprojects/ifbb/ifbb.ru/www/media/ckeditor'
    PAGES_URL = 'http://new3.ifbb.ru/pages/'
    MEDIA_ROOT = '/home/c6582/www/media/'

else:
   STATIC_ROOT ='C:/djprojects/ifbb/ifbb.ru/www/static'
   CKEDITOR_UPLOAD_PATH = '/media/ckeditor'
   PAGES_URL = 'http://localhost:8000/pages/'
   MEDIA_ROOT = 'C:/djprojects/ifbb/ifbb.ru/www/media'













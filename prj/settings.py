import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Debug settings (make sure to set to False in production/deploys)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Must be specified (make it good and long/random!)
SECRET_KEY = ''
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wishlist'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'prj.urls'
WSGI_APPLICATION = 'prj.wsgi.application'

# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Database configuration. Be sure to add production values (including safe password!)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangowishlist',
        'USER': 'djangowishlist',
        'PASSWORD': 'djangowishlist',
        'HOST': '' #localhost
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + "/publish/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'prj/static'),
)

TEMPLATE_DIRS = (
    BASE_DIR + "templates/",
)

# Local settings overrides (store your own values for DB / SECRET in local_seetings.py)
try: from local_settings import *
except: pass # pylint: disable-msg=W0702

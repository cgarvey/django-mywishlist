import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Debug settings (make sure to set to False in production/deploys)
DEBUG = True

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

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages'
        ],
    },
}]

# TEMPLATE_DIRS = (
#     BASE_DIR + "templates/",
# )

# Local settings overrides (store your own values for DB / SECRET in local_seetings.py)
try: from .local_settings import *
except: pass # pylint: disable-msg=W0702

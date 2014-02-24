"""
Django settings for Co_Trip project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4*hff8(zx-%t6@n42awk$w13ee)+m+xpy52d_!e6r-wzphe#^a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ajax_select',
    'django.contrib.humanize',
    #'django.contrib.sites',
    #'south'
    'registration',
    'plan',
    'traveller',
    'Co_Trip',
    'cities_light',
    'guardian',
    'bootstrap3',
    'bootstrap3_datetime',
    'api',
    'tastypie',
    'notifications',
    'south',

)

AJAX_LOOKUP_CHANNELS = {
    'cities_light_country': ('cities_light.lookups', 'CountryLookup'),
    'cities_light_city': ('cities_light.contrib.ajax_selects_lookups', 'CityLookup'),
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Co_Trip.urls'

WSGI_APPLICATION = 'Co_Trip.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'danielqiu',
        'PASSWORD': '123456',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
)

ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'admin@h1994st.com'
DEFAULT_FROM_EMAIL = 'admin@h1994st.com'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

AUTH_PROFILE_MODULE = 'traveller.Traveller'

GUARDIAN_RAISE_403 = True

CITIES_LIGHT_TRANSLATION_LANGUAGES = ['ZH']
CITIES_LIGHT_TRANSLATION_SOURCES = ['http://download.geonames.org/export/dump/CN.zip']

ADMINS = (('qsz13', 'qsz1328@gmail.com'))

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
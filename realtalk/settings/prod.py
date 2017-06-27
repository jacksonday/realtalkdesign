"""Development settings and globals."""
from .common import *
from os import environ
import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

PRODUCTION = True


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)
print(os.environ.get('SECRET_KEY'))
########## END SECRET CONFIGURATION

ALLOWED_HOSTS = ['realtalkdesign.herokuapp.com']

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

MIDDLEWARE_CLASSES += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
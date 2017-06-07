"""Development settings and globals."""
from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

PRODUCTION = True


ALLOWED_HOSTS = ['realtalkdesign.herokuapp.com']

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

MIDDLEWARE_CLASSES += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#STATIC_ROOT = "/home/cfedeploy/webapps/cfehome_static_root/"
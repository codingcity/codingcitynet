from .base import *

ALLOWED_HOSTS = ['54.164.103.70','codingcity.net','www.codingcity.net']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

MEDIA_ROOT =  BASE_DIR / 'media/'
"""
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


#for media
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'_media')

"""
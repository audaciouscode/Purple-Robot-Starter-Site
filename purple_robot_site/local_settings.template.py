
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE_ME'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = [('Your Name', 'you@email.com')]
ALLOWED_HOSTS = [ 'your.site.com' ]

DATABASES = {
	'default': {
		'ENGINE':   'django.contrib.gis.db.backends.postgis',
		'NAME':     '',
		'USER':     '',
		'PASSWORD': '',
		'HOST':     'localhost',
		'PORT':     '',
	}
}

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.contrib.gis.db.backends.postgis',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }

PURPLE_ROBOT_DISABLE_DATA_CHECKS = False
PURPLE_ROBOT_SITE_PREFIX = 'changeme'
PURPLE_ROBOT_SHOW_DEVICE_ID_HEADER = False
PURPLE_ROBOT_SHOW_NOTES = False
URL_PREFIX = 'https://my.purple-robot.com/'
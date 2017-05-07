import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE_ME'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = [('Your Name', 'you@email.com')]
ALLOWED_HOSTS = [ 'your.site.com' ]

DATABASES = {
	'default': {
		'ENGINE':   'django.db.backends.postgresql_psycopg2',
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
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }

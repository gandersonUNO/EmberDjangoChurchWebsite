# Set to DEV for debug and other configuration items.  PROD otherwise...
ENVIRONMENT = 'PROD'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<insert secret key here>'

#ROOT_URLCONF = 'urls'
ROOT_URLCONF = 'django_backend.urls'
WSGI_APPLICATION = 'django_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '******',
        'USER': '******',
        'PASSWORD':'*****',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

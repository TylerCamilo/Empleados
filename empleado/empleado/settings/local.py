from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
print('HOLA SOY EL AMBIENTE LOCAL')

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'camilo',
        'PASSWORD' : 'C4m1L0',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
#Elcurso sugiere la siguiente linea de codigo
#STATICFILES_DIR = [BASE_DIR.child('static')]
#Pero en documentacion funciona de la siguiente manera
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]


from .common import *
from environs import Env


env = Env()
env.read_env()


DEBUG = env.bool('DJANGO_DEBUG')

#we shouldnt add silk middlware in original middleware because its for production too,we use silk just for developement and another resean is it adds alot of overhead to each request,,so we add it if debug is true
if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']


SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'HOST': env('DATABASE_HOST'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD')
    }
}

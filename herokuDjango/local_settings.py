import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '=+e9uk-h2a!t6+ej(c8cwk$e-+7i=s0#rvchshug+p$np2zi1q'

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True #ローカルでDebugできるようになります
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
ALLOWED_HOSTS = ['*'] #こちらでもokです
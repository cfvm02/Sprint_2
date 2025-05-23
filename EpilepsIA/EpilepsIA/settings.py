"""
Django settings for EpilepsIA project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&3_a6n$7c26y%#vtmuarp_h9-s$c7j%2-j201_cjszbm)(+@#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Examen',
    'miRNA',
    'MRI',
    'EEG',
    'Alerta',
    'AlertaDiagnostico',
    'AlertaResultado',
    'Evento',
    'Medico',
    'Paciente',
    'Resultado',
    'Solicitud',
    'social_django',
'corsheaders'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'EpilepsIA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EpilepsIA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'epilepsia_db',
	'USER': 'isis2503',
	'PASSWORD': 'isis2503',
	'HOST': '10.128.0.3',
	'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:4200',
#     'http://192.168.88.1:4200',
# ]



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/isis2503/llave_privada_arqui.json"

# Configuración del bucket de Google Cloud Storage
GCS_BUCKET_NAME = "examenes-eeg"  # Reemplaza con el nombre real de tu bucket
GCS_BASE_FOLDER = "uploads/"  # Opcional: carpeta base en el bucket para tus archivos

#FILE_UPLOAD_MAX_MEMORY_SIZE = 500 * 1024 * 1024  # 500 MB (si usas archivos)
#DATA_UPLOAD_MAX_MEMORY_SIZE = 500 * 1024 * 1024  # 500 MB

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://dev-qox2s5e2aky6aehb.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F104.154.186.35:4200"

SOCIAL_AUTH_TRAILING_SLASH = False # Remove end slash from routes 
SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-qox2s5e2aky6aehb.us.auth0.com' 
SOCIAL_AUTH_AUTH0_KEY = 'u8GVzzzDieeY1kKnhCUnVx0IT0xYXOn8' 
SOCIAL_AUTH_AUTH0_SECRET = 'rEyASvcOXVtlnwdqH0FsqIPXbIHNyMM1FxYOSjz_UlnZO_-Pp2mn_2ZzHQccIoOE' 

SOCIAL_AUTH_AUTH0_SCOPE = [ 'openid', 
                           'profile', 
                           'email', 
                           'role', ] 
AUTHENTICATION_BACKENDS = { 'monitoring.auth0backend.Auth0', 
                           'django.contrib.auth.backends.ModelBackend', }
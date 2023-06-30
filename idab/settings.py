"""
Django settings for idab project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import datetime
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qd#6&xs7i(y0_w*^mgx9leh42*f&h@&24y3q24)t!a^e9&f4yl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.idab.mba', 'idab.mba', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Admin sorting
    'adminsortable2',
    # Debug Tool Bar
    'debug_toolbar',
    # django-extensions
    'django_extensions',
    # phone numbers field
    'phonenumber_field',
    # Package for user registration and authentication endpoints
    'djoser',
    # rest API implementation library for django
    'rest_framework',
    # Django Filters
    'django_filters',
    # swagger
    'drf_yasg',
    # JWT authentication backend library
    'rest_framework_simplejwt',
    # CKEDITOR
    'ckeditor',
    'ckeditor_uploader',
    # corsheaders
    'corsheaders',
    # Import-Export
    'import_export',
    # my apps
    'users.apps.UsersConfig',
    'programs.apps.ProgramsConfig',
    'courses.apps.CoursesConfig',
    'checkpoints.apps.CheckpointsConfig',
    'tutorials.apps.TutorialsConfig',
    'siteblocks.apps.SiteblocksConfig',
    'news.apps.NewsConfig',
    'bids.apps.BidsConfig',
    'schedule.apps.ScheduleConfig',
    'galleries.apps.GalleriesConfig',
    'tasks.apps.TasksConfig',
    'library.apps.LibraryConfig',
    'studymaterials.apps.StudymaterialsConfig',
    'slack.apps.SlackConfig',
    'attendances.apps.AttendancesConfig',
    'ratings.apps.RatingsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'idab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend/build',
        os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'idab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'idab',
        'USER': 'idabadmin',
        'PASSWORD': 'idabsecret',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'idab.guu@gmail.com'
EMAIL_HOST_PASSWORD = 'obbaayuqtiorlvdr'
EMAIL_USE_TLS = True


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PHONENUMBER_DB_FORMAT = 'RFC3966'
PHONENUMBER_DEFAULT_REGION = 'RU'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/admin-static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'admin-static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'frontend/build/static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'idab/static'),
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = "uploads/"

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=14)
}

# Djoser
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': False,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'SET_USERNAME_RETYPE': False,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'user': 'users.serializers.MyUserCreateSerializer',
        'current_user': 'users.serializers.MyUserCreateSerializer',
        'user_create': 'users.serializers.MyUserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}

AUTH_USER_MODEL = 'users.User'
SITE_ID = 1

INTERNAL_IPS = [
    '127.0.0.1',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

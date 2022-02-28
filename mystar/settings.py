"""
Django settings for mystar project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "t&9&8r+xs5s1+f)jfp9#4=84a*ms(#+(022#lv6fh!kt-nfhvc"
# SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "mystargoods.herokuapp.com",
    "mymyprint.herokuapp.com",
    "www.mymyprint.net",
    "mymyprint.net",
    "api.mymyprint.net",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "cloudinary_storage",
    "djmoney",
    "rest_framework",
    "corsheaders",
    "pictures",
    "rest_framework.authtoken",
    "rest_framework_api_key",
    "rest_auth",
    "django_summernote",
    "profiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_auth.registration",
    "imagekit",
    "whitenoise.runserver_nostatic",
    "cloudinary",
    "storages",
    # "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "mystar.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "build")],
        # "DIRS": [
        #     "templates",  # <- here
        # ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mystar.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mystar",
        "USER": "mystar",
        "PASSWORD": "mystargoods!@#",
        "HOST": "localhost",
        "PORT": "",
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "/static")]
# STATIC_ROOT = os.path.join(BASE_DIR, "build/static")
STATIC_ROOT = "/srv/build/static"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = "/media/"
# MEDIA_DIRS = [os.path.join(BASE_DIR, "/media")]
MEDIA_ROOT = os.path.join(BASE_DIR, "/media")
# MEDIA_ROOT = "/srv/media"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_api_key.permissions.HasAPIKey",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 12,
}

X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_THEME = "bs4"
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
AUTH_USER_MODEL = "profiles.CustomUser"
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "profiles.api.serializers.UserSerializer",
}
ACCOUNT_ADAPTER = "profiles.adapters.CustomUserAccountAdapter"
# CSRF_TRUSTED_ORIGINS = (
#     "0.0.0.0",
#     "localhost",
#     "127.0.0.1",
#     "mystargoods.herokuapp.com",
#     "mymyprint.herokuapp.com",
#     "www.mymyprint.net",
#     "mymyprint.net",
#     "api.mymyprint.net",
# )

# CORS_ORIGIN_WHITELIST = (
#     "0.0.0.0",
#     "localhost",
#     "127.0.0.1",
#     "mystargoods.herokuapp.com",
#     "mymyprint.herokuapp.com",
#     "www.mymyprint.net",
#     "mymyprint.net",
#     "api.mymyprint.net",
# )

CORS_ALLOW_HEADERS = (
    "access-control-allow-credentials",
    "access-control-allow-origin",
    "access-control-request-method",
    "access-control-request-headers",
    "accept",
    "accept-encoding",
    "accept-language",
    "authorization",
    "connection",
    "content-type",
    "dnt",
    "credentials",
    "host",
    "origin",
    "user-agent",
    "X-CSRFToken",
    "csrftoken",
    "x-requested-with",
)
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "profiles.api.serializers.MyRegisterSerializer",
}
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'

SITE_ID = 1
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ACCOUNT_AUTHENTICATION_METHOD = "email"
API_KEY_CUSTOM_HEADER = "HTTP_MYSTAR_API_KEY"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "hjgc6h8kn",
    "API_KEY": "242999711416721",
    "API_SECRET": "TwOdTgmO4UjTeh8PzIqNfBtTmVo",
}
AWS_ACCESS_KEY_ID = "AKIAZB4ANSYHEIOMA7XE"  # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = (
    "5tm3qEFKguMYIHynQcePr5TJqM+d7BjG4rosHgCd"  # .csv 파일에 있는 내용을 입력 Secret access key
)
AWS_REGION = "ap-northeast-2"

###S3 Storages
AWS_STORAGE_BUCKET_NAME = "mystar-image"  # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
DEFAULT_FILE_STORAGE = "mystar.storage_backends.CustomS3Boto3Storage"
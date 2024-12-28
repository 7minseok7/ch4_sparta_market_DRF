"""
Django settings for spartamarket_DRF project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-54&34bm4nqpl6gxkk07$siz27$49q&=1%k@8ph0mk^l14sxqyl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 장고 REST Framework
    'rest_framework',

    # 써드파티 앱
    'django_seed',

    # 로컬 앱
    'accounts',
    'products',
]

# DRF에서 JWT 인증 관련 클래스 추가
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

from datetime import timedelta
...

# JWT 관련 설정
SIMPLE_JWT = {
    # 평소에 API 통신할 때는 Access Token을 사용. 여기서는 테스트를 위해 30분 동안 유효하도록 해 둠.
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),

    # Refresh Token은 Access Token이 만료되어 이를 갱신할 때만 사용. 여기서는 하루 동안 유효하도록 해 둠.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    
    # 즉, 통신과정에서 탈취당할 위험이 큰 Access Token의 만료 기간을 짧게 두고 Refresh Token으로 주기적으로 재발급함으로써 피해을 최소화한 것이다.
    
    # ROTATE_REFRESH_TOKENS:
    # True로 설정할 경우 simplejwt_token 앱에서 제공하는 TokenRefreshView에 리프레시 토큰을 제출할 때 
    # 액세스 토큰과 리프레시 토큰 둘 다 재발급을 받는다. False 일경우 액세스 토큰만 재발급 받는다.
    "ROTATE_REFRESH_TOKENS": True,

    # BLACKLIST_AFTER_ROTATION: True로 설정할 경우, ROTATE_REFRESH_TOKENS 이 True 일 때, TokenRefreshView에 제출된 리프레시 토큰은 블랙리스트에 추가된다.
    "BLACKLIST_AFTER_ROTATION": True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spartamarket_DRF.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'spartamarket_DRF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = "accounts.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"  # 배포 시에 작동함. 개발 단계에서는 의미 없음.

# 미디어 처리 관련
MEDIA_URL = "/media/"
BASE_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

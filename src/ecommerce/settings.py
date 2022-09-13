
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w#*9gr*6q$k_6esrdi=7jy7j63u&0!28^6svfsf+91wms0ft7)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'social_django', # to social login
    'about',
    'products',
    'contact',
    # 'django_social_share', # for sharing links to social sites
]

# AUTH_USER_MODEL ='accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'about.footer_context_processor.shopinfo',
                'products.nav_context_processor.navinfo',
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',

)

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_GITHUB_KEY = '42d9be03d377c15a8ca3'
SOCIAL_AUTH_GITHUB_SECRET = '010953e8e3cfd4bd7a413370e76c2c718745e349'

# github information
# Client ID
# 42d9be03d377c15a8ca3
# Client secrets
# 010953e8e3cfd4bd7a413370e76c2c718745e349
# https://github.com/settings/applications/1980199   # to manage next data
#     Homepage URL : http://127.0.0.1:8000/
#     Authorization callback URL : http://localhost:8000/


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '51450330573-u2dtfcdlmdggs6c24tplg23v3admrj4n.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# google information
# Client ID
    # 51450330573-u2dtfcdlmdggs6c24tplg23v3admrj4n.apps.googleusercontent.com
# Client secrets
    # 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
# https://console.cloud.google.com/apis/credentials/oauthclient/51450330573-u2dtfcdlmdggs6c24tplg23v3admrj4n.apps.googleusercontent.com?project=trendy-360504   # to manage next data
    # Authorized JavaScript origins : http://127.0.0.1:8000/
    # Authorization callback URL : http://localhost:8000/oauth/complete/google-oauth2/

SOCIAL_AUTH_TWITTER_KEY = '6Ywgtjioc0VwpB67nvayJoOpx'
SOCIAL_AUTH_TWITTER_SECRET = 'pDXlxCBIm7bJI0oXLcYfuqZJb7kkBSmBkAVDjGcGOIJ81NxuDs'


# twitter information
# Client ID
    # 6Ywgtjioc0VwpB67nvayJoOpx
# Client secrets
    # pDXlxCBIm7bJI0oXLcYfuqZJb7kkBSmBkAVDjGcGOIJ81NxuDs
# bearer token
    # AAAAAAAAAAAAAAAAAAAAAJJ1gQEAAAAA6xD6ENyuVbHpkWrVZ6Z98Q0N638%3D8RgADonHdILqB1qhmZCVInCJ5QsdcgkrvvBmxWh8rFvVq6CILV
# https://developer.twitter.com/en/portal/projects/1562861197971533825/apps/25261458/settings
    # Authorized JavaScript origins : http://trendy.com  # any valid name
    # Authorization callback URL : http://localhost:8000/oauth/complete/twitter/




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/',
]
MEDIA_URL = '/media/'
MEDIA_ROOT=BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'platraincloud@gmail.com'
EMAIL_HOST_PASSWORD = 'meczfpooichwkudl'
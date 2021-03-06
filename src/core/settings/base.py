import os

from pathlib import Path

# Build paths like this str(PROJECT_ROOT / 'foo' / 'bar')
PROJECT_ROOT = Path(__file__).resolve().parents[3]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This is what we use to prefix dbs and cache keys etc
DEPLOY_ENV = os.environ['DEPLOY_ENV']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'asjofasfbasufbasiufuiasbfuiasbf'

# Application definition
INSTALLED_APPS = [
    'webpack_loader',
    'core',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
]

MIDDLEWARE = [
    'core.middleware.AppendSlashMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en-gb', 'English'),
]

DEFAULT_LANGUAGE = 'en-gb'


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.request',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
        ],
        'loaders': [
            'django.template.loaders.app_directories.Loader',
        ],
        'debug': DEBUG
    }
}]

WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(str(PROJECT_ROOT), 'frontend', 'config', 'webpack-stats.dev.json'),
        }
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True


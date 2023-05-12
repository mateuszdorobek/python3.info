import os
from datetime import timedelta, datetime, timezone

from django.conf.locale.en import formats as en_formats
from django.core.exceptions import ImproperlyConfigured

# Load settings from system environment variables
try:
    DEBUG = os.environ.get('DJANGO_DEBUG', False)
    DEBUG_TOOLBAR = os.environ.get('DJANGO_DEBUG_TOOLBAR', False)
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'this_is_default_key_please_change_it_using_env_variable')
    ALLOWED_HOST = os.environ.get('DJANGO_ALLOWED_HOST', 'localhost')
    SECURE_SSL_REDIRECT = os.environ.get('DJANGO_ALWAYS_HTTPS', False)

    # Make sure, you also change conf/nginx.conf
    MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT', '/tmp/media')
    STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '/tmp/static')
    MEDIA_URL = os.environ.get('DJANGO_MEDIA_URL', '/media/')
    STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')

    DATABASE_ENGINE = os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3')
    DATABASE_HOST = os.environ.get('DATABASE_HOST', None)
    DATABASE_PORT = os.environ.get('DATABASE_PORT', None)
    DATABASE_NAME = os.environ.get('DATABASE_NAME', '/tmp/habitatOS/db.sqlite3')
    DATABASE_USER = os.environ.get('DATABASE_USER', None)
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', None)

    HABITATOS_MISSION_NAME = os.environ.get('HABITATOS_MISSION_NAME', None)
    HABITATOS_DELAY_SECONDS = os.environ.get('HABITATOS_DELAY_SECONDS', 0)
    HABITATOS_MISSION_START = os.environ.get('HABITATOS_MISSION_START', '2000-01-01T00:00:00Z')
    HABITATOS_MISSION_END = os.environ.get('HABITATOS_MISSION_END', '2000-02-01T00:00:00Z')
    HABITATOS_TIME_ZONE = os.environ.get('HABITATOS_TIME_ZONE', 'habitat.time.MissionElapsedTime')
    HABITATOS_SCHEDULE_URL = os.environ.get('HABITATOS_SCHEDULE_URL', None)

    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'habitatOS')
    AWS_S3_BUCKET_NAME_STATIC = os.environ.get('AWS_S3_BUCKET_NAME_STATIC', 'habitatOS')
    AWS_S3_HOST = os.environ.get('AWS_S3_HOST', None)
    AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID', None)
    AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY', None)

    GOOGLE_ANALYTICS_CODE = os.environ.get('GOOGLE_ANALYTICS_CODE', None)

except KeyError as e:
    raise ImproperlyConfigured(f'You must set {e} environment variable. Please refer to the habitatOS documentation.')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'habitat.urls'
WSGI_APPLICATION = 'habitat.wsgi.application'
ALLOWED_HOSTS = [ALLOWED_HOST, '192.168.8.2', '192.168.8.3']

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'storages',
    'emoji_picker',
    # 'rosetta',

    'habitat._common',
    'habitat.menu.MenuConfig',
    'habitat.authorization.apps.AuthorizationConfig',
    'habitat.feedback.apps.FeedbackConfig',
    'habitat.system.apps.SystemConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'habitat.biolab.apps.BiolabConfig',
    'habitat.building.apps.BuildingConfig',
    'habitat.communication.apps.CommunicationConfig',
    'habitat.extravehicular.apps.ExtravehicularConfig',
    'habitat.food.apps.FoodConfig',
    'habitat.health.apps.HealthConfig',
    'habitat.workout.apps.WorkoutConfig',
    'habitat.inventory.apps.InventoryConfig',
    'habitat.notification.apps.NotificationsConfig',
    'habitat.reporting.apps.ReportingConfig',
    'habitat.sensors.apps.SensorsConfig',
    'habitat.time.apps.TimezoneConfig',
    'habitat.water.apps.WaterConfig',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages']}
}]


# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'authorization.User'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

if SECURE_SSL_REDIRECT == 'True':
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 3600
else:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 0

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

en_formats.DATETIME_FORMAT = 'Y-m-d H:i'
en_formats.DATE_FORMAT = 'Y-m-d'
en_formats.TIME_FORMAT = 'H:i'
TIME_INPUT_FORMATS = ['%H:%M', '%H:%M:%S']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'list',
    'OPERATIONS_SORTER': 'alpha',
    'api_version': '1.0',
}

LOGGING = {}


MEGABYTE = 1_000_000
# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 100 * MEGABYTE

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = 100 * MEGABYTE

MEDIA_LOCATION = 'media'
STATIC_LOCATION = 'static'

HABITATOS = {
    'MISSION_NAME': HABITATOS_MISSION_NAME,
    'DELAY': timedelta(seconds=int(HABITATOS_DELAY_SECONDS)),
    'MISSION_START': datetime.strptime(HABITATOS_MISSION_START, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc),
    'MISSION_END': datetime.strptime(HABITATOS_MISSION_END, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc),
    'TIME_ZONE': HABITATOS_TIME_ZONE,
    'SCHEDULE_URL': HABITATOS_SCHEDULE_URL,
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': int(DATABASE_PORT) if DATABASE_PORT else None,
    }
}

if os.path.exists('/tmp/habitatOS/memcached.sock'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
            'LOCATION': '/tmp/habitatOS/memcached.sock',

            # Use binary memcache protocol (needed for authentication)
            'BINARY': True,

            # TIMEOUT is not the connection timeout! It's the default expiration
            # timeout that should be applied to keys! Setting it to `None`
            # disables expiration.
            'TIMEOUT': None,

            'OPTIONS': {
                # Enable faster IO
                'tcp_nodelay': True,

                # Keep connection alive
                'tcp_keepalive': True,

                # Timeout settings
                'connect_timeout': 2000,  # ms
                'send_timeout': 750 * 1000,  # us
                'receive_timeout': 750 * 1000,  # us
                '_poll_timeout': 2000,  # ms

                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30,
            }
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


AWS_S3_BUCKET_AUTH = False
AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365  # 1 year.
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False

if AWS_S3_SECRET_ACCESS_KEY:
    DEFAULT_FILE_STORAGE = 'habitat.system.storage.MediaStorage'
    STATICFILES_STORAGE = 'habitat.system.storage.StaticStorage'
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


if DEBUG_TOOLBAR == 'True':
    DEBUG_TOOLBAR = True
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']
else:
    DEBUG_TOOLBAR = False


if DEBUG == 'True':
    DEBUG = True
    ALLOWED_HOSTS.append('127.0.0.1')
    ALLOWED_HOSTS.append('localhost')
    MIDDLEWARE += ['habitat._common.middleware.cache.DisableBrowserCache']
else:
    DEBUG = False

import os
import pathlib

# Build paths inside the project like this: BASE_DIR / "subdir"
BASE_DIR = pathlib.Path(__file__).resolve().parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "a87082n4v52u4rnvk2edv128eudfvn5"  # noqa: S105

ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TESTING = False

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "django_probes",
    "django_extensions",
    "import_export",
    "import_export_extensions",
    "test_project.fake_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "test_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "test_project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DB_HOST = os.environ.get("DB_HOST", "postgres")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
        "USER": "django-import-export-extensions-user",
        "NAME": "django-import-export-extensions-dev",
        "PASSWORD": "testpass",
        "HOST": DB_HOST,
        "PORT": 5432,
    },
}

AUTH_USER_MODEL = "auth.User"

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Configure `drf-spectacular` to check it works for import-export API
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "COMPONENT_SPLIT_REQUEST": True,  # Allows to upload import file from Swagger UI
}

# Don't use celery when you're local
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_STORE_EAGER_RESULT = True

CELERY_TASK_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ["pickle", "json"]

CELERY_TASK_ROUTES = {}
CELERY_BROKER = os.environ.get("REDIS_HOST", "redis://redis/1")
CELERY_BACKEND = os.environ.get("REDIS_HOST", "redis://redis/1")
CELERY_TASK_DEFAULT_QUEUE = "development"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler"},
    },
    "loggers": {
        "django.db.backends": {"level": "INFO", "handlers": ["console"]},
        "django.request": {
            "handlers": ["console"],
            "propagate": False,
            "level": "ERROR",
        },
        "account": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "import_export": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "import_export_extensions": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


if DEBUG:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

    def _show_toolbar_callback(request) -> bool:
        """Show debug toolbar exclude testing."""
        from django.conf import settings

        return not settings.TESTING

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": _show_toolbar_callback,
    }

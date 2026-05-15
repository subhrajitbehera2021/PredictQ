import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
import dj_database_url


# =========================================================
# BASE DIRECTORY
# =========================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# =========================================================
# LOAD ENV VARIABLES
# =========================================================
load_dotenv(BASE_DIR / ".env")


# =========================================================
# SECURITY
# =========================================================
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-queuesense-secret-key"
)

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,.onrender.com"
).split(",")

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]


# =========================================================
# INSTALLED APPS
# =========================================================
INSTALLED_APPS = [

    # =====================================================
    # DJANGO APPS
    # =====================================================
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # =====================================================
    # THIRD PARTY APPS
    # =====================================================
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "channels",

    # =====================================================
    # LOCAL APPS
    # =====================================================
    "apps.core",
    "apps.users",
    "apps.hospitals",
    "apps.departments",
    "apps.authentication",
    "apps.doctors",
    "apps.schedules",
    "apps.bookings",
    "apps.queue_management",
    "apps.staff_management",
    "apps.notifications",
    "apps.analytics",
    "apps.audit_logs",
    "apps.ai_gateway",
    "apps.patients",
    "apps.appointments"
]

AUTH_USER_MODEL = "users.User"


# =========================================================
# MIDDLEWARE
# =========================================================
MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "apps.audit_logs.middleware.AuditLogMiddleware",

    "apps.core.middleware.RequestLoggingMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# ROOT URLS
# =========================================================
ROOT_URLCONF = "config.urls"


# =========================================================
# TEMPLATES
# =========================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [BASE_DIR / "templates"],

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


# =========================================================
# WSGI
# =========================================================
WSGI_APPLICATION = "config.wsgi.application"


# =========================================================
# DATABASE
# =========================================================
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:password@localhost:5432/queuesense_db"
        ),
        conn_max_age=600,
        ssl_require=False
    )
}


# =========================================================
# PASSWORD VALIDATION
# =========================================================
AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================
STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# =========================================================
# MEDIA FILES
# =========================================================
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================
REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": (

        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    "DEFAULT_PERMISSION_CLASSES": (

        "rest_framework.permissions.AllowAny",
    ),
}


# =========================================================
# CHANNEL LAYERS
# =========================================================
CHANNEL_LAYERS = {

    "default": {

        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}


# =========================================================
# CORS
# =========================================================
CORS_ALLOW_ALL_ORIGINS = True


# =========================================================
# SIMPLE JWT
# =========================================================
SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),

    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),

    "ROTATE_REFRESH_TOKENS": True,

    "BLACKLIST_AFTER_ROTATION": True,

    "UPDATE_LAST_LOGIN": True,
}
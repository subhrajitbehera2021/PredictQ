from .base import *
import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}
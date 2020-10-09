"""local runserver settings"""
​
import os
from .settings import BASE_DIR
​
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*jofgwu+lpmy3ngd+&v@1fmp)3)^o+%t7v*stu=b@d5!_cqd+h"
​
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
​
ALLOWED_HOSTS = []
​
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
​
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
​
# Static Files
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

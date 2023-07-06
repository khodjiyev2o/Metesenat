from .base import *  # noqa


STAGE = "develop"
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": (BASE_DIR / "db.sqlite3"),
    }
}

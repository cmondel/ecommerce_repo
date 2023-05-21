from .base import BASE_DIR
from .base import load_dotenv

load_dotenv()
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

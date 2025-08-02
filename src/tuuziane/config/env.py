from smart_env import SmartEnv

DEFAULTS = {
    "ALLOWED_HOSTS": (list, ["localhost", "127.0.0.1"]),
    "ADMIN_PANEL_URL": (str, "rabangaha"),
    "AWS_ACCESS_KEY_ID": (str, "somekeys"),
    "AWS_S3_CUSTOM_DOMAIN": (str, "localhost"),
    "AWS_S3_ENDPOINT_URL": (str, "some values"),
    "AWS_SECRET_ACCESS_KEY": (str, "some values"),
    "AWS_STORAGE_BUCKET_NAME": (str, "some values"),
    "DATABASE_URL": (str, "sqlite:///db.sqlite3"),
    "DEBUG": (bool, False),
    "DEFAULT_FROM_EMAIL": (str, "webmaster@localhost"),
    "DOMAIN": (str, "http://localhost:8000"),
    "EMAIL_HOST": (str, ""),
    "EMAIL_HOST_USER": (str, ""),
    "EMAIL_HOST_PASSWORD": (str, ""),
    "EMAIL_PORT": (str, ""),
    "EMAIL_USE_TLS": (bool, True),
    "SECRET_KEY": (str, "your-default-secret-key"),
    "SOCIALACCOUNT_PROVIDERS": (
        dict,
        {
            "google": {"APP": {"client_id": "", "secret": "", "key": ""}},
            "facebook": {"APP": {"client_id": "", "secret": "", "key": ""}},
        },
    ),
    "WAGTAILADMIN_BASE_URL": (str, "http://localhost"),
}

env = SmartEnv(**DEFAULTS)

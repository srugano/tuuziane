import os
from oscar.defaults import *  # noqa: F403
from tuuziane.config.env import env
import dj_database_url

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DOMAIN_NAME = env("DOMAIN")
WWW_ROOT = f"http://{DOMAIN_NAME}/"
FRONTEND_HOST = env("DOMAIN")
ADMIN_PANEL_URL = env("ADMIN_PANEL_URL")
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
# Paths and directories
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(PROJECT_DIR))

# Core Django settings
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DOMAIN_NAME = env("DOMAIN")
WWW_ROOT = f"http://{DOMAIN_NAME}/"
FRONTEND_HOST = env("DOMAIN")
ADMIN_PANEL_URL = env("ADMIN_PANEL_URL")
SITE_ID = 1
ROOT_URLCONF = "tuuziane.urls"
WSGI_APPLICATION = "tuuziane.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
APPEND_SLASH = True
INSTALLED_APPS = [
    "tuuziane.core",
    "rest_framework",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "haystack",  # Required for search https://docs.wagtail.org/en/stable/reference/management_commands.html#wagtail-update-index
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "allauth",
    "allauth.account",
    "allauth.socialaccount.providers.apple",
    "allauth.socialaccount.providers.auth0",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.instagram",
    "allauth.socialaccount.providers.linkedin_oauth2",
    "allauth.socialaccount.providers.microsoft",
    "allauth.socialaccount.providers.paypal",
    "allauth.socialaccount.providers.shopify",
    "allauth.socialaccount.providers.slack",
    "allauth.socialaccount.providers.telegram",
    "allauth.socialaccount.providers.weibo",
    "oscar.config.Shop",
    "oscar.apps.analytics.apps.AnalyticsConfig",
    "oscar.apps.checkout.apps.CheckoutConfig",
    "oscar.apps.address.apps.AddressConfig",
    "oscar.apps.shipping.apps.ShippingConfig",
    "tuuziane.apps.catalogue.apps.CatalogueConfig",
    "oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "oscar.apps.communication.apps.CommunicationConfig",
    "oscar.apps.partner.apps.PartnerConfig",
    "oscar.apps.basket.apps.BasketConfig",
    "oscar.apps.payment.apps.PaymentConfig",
    "oscar.apps.offer.apps.OfferConfig",
    "oscar.apps.order.apps.OrderConfig",
    "oscar.apps.customer.apps.CustomerConfig",
    "oscar.apps.search.apps.SearchConfig",
    "oscar.apps.voucher.apps.VoucherConfig",
    "oscar.apps.wishlists.apps.WishlistsConfig",
    "oscar.apps.dashboard.apps.DashboardConfig",
    "oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "oscar.apps.dashboard.users.apps.UsersDashboardConfig",
    "oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
    "oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
    "oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",
    "webpack_loader",
    "widget_tweaks",
    "treebeard",
    "sorl.thumbnail",
    "django_tables2",
    "django_user_agents",
    "django_extensions",
    "oscarapi",
    "tuuziane.apps.homepage",
    "health_check",  # required
    "health_check.db",  # stock Django health checkers
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    "health_check.contrib.psutil",  # disk and memory utilization; requires psutil
]

SITE_ID = 1

MIDDLEWARE = [
    "oscarapi.middleware.ApiGatewayMiddleWare",
    # "django.contrib.sessions.middleware.SessionMiddleware",
    "oscarapi.middleware.HeaderSessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "oscarapi.middleware.ApiBasketMiddleWare",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "tuuziane.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "oscar.apps.search.context_processors.search_form",
                "oscar.apps.checkout.context_processors.checkout",
                "oscar.apps.communication.notifications.context_processors.notifications",
                "oscar.core.context_processors.metadata",
                "tuuziane.context_processors.oscar_shop_tagline",
            ],
        },
    },
]

WSGI_APPLICATION = "tuuziane.wsgi.application"


# Database
DATABASES = {"default": dj_database_url.config(default=env("DATABASE_URL"))}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
    os.path.join(BASE_DIR, "src", "frontend", "dist"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = f"/{env('STATIC_PATH_NAME')}/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
if env("STORAGE_TYPE") != "s3":
    MEDIA_URL = f"/{env('MEDIA_PATH_NAME')}/"

# Storage configuration
if env("STORAGE_TYPE") == "s3":
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "location": env("MEDIA_PATH_NAME"),
                "file_overwrite": False,
            },
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
        },
    }
    MEDIA_URL = f"https://{env('AWS_S3_CUSTOM_DOMAIN')}/"
else:
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }


# Wagtail settings

WAGTAIL_SITE_NAME = "tuuziane"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = env("WAGTAILADMIN_BASE_URL")

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = [
    "csv",
    "docx",
    "key",
    "odt",
    "pdf",
    "pptx",
    "rtf",
    "txt",
    "xlsx",
    "zip",
]

AUTHENTICATION_BACKENDS = (
    "oscar.apps.customer.auth_backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

OSCAR_SHOP_NAME = "Tuuziane"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
        # "ENGINE": "haystack.backends.solr_backend.SolrEngine",
        # "URL": "http://127.0.0.1:8983/solr/sandbox",
        # "ADMIN_URL": "http://127.0.0.1:8983/solr/admin/cores",
        # "INCLUDE_SPELLING": True,
        # "COMMIT_WITHIN": 500,
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
OSCAR_THUMBNAIL_DEBUG = DEBUG

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "haystack": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}


OSCAR_INITIAL_ORDER_STATUS = "Pending"
OSCAR_INITIAL_LINE_STATUS = "Pending"
OSCAR_ORDER_STATUS_PIPELINE = {
    "Pending": (
        "Being processed",
        "Cancelled",
    ),
    "Being processed": (
        "Processed",
        "Cancelled",
    ),
    "Cancelled": (),
}
OSCARAPI_PRODUCT_FIELDS = ["url", "id", "upc", "title", "price", "stockrecords", "images"]
OSCARAPI_ENABLE_REGISTRATION = True

APPEND_SLASH = True


WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "src", "frontend", "dist", "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "tuuziane.apps.core.pagination.StandardPagination",
}

SOCIALACCOUNT_PROVIDERS = env("SOCIALACCOUNT_PROVIDERS")

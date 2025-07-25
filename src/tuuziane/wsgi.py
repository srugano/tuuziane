"""
WSGI config for tuuziane project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# The `tuuziane` app is now in `src/`, so we need to add `src/` to the path
# so that the wsgi server can find it.
# __file__ is /path/to/project/src/tuuziane/wsgi.py
# so its parent's parent is /path/to/project/src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuuziane.settings.dev")

application = get_wsgi_application()

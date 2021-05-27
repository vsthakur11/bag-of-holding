"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
password="Vikram321"
key="Par@3221"
standenc="AES256"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")
application = get_wsgi_application()

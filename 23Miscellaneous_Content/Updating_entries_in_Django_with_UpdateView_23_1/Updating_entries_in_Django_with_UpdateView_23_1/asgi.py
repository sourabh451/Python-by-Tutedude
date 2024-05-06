"""
ASGI config for Updating_entries_in_Django_with_UpdateView_23_1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Updating_entries_in_Django_with_UpdateView_23_1.settings')

application = get_asgi_application()

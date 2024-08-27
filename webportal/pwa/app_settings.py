""" Settings required by django-app. """
from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import get_script_prefix
from django.utils.functional import lazy
import os

# Lazy-evaluate URLs so including pwa.urls in root urlconf works
resolve_url = lazy(resolve_url, str)

# Get script prefix for apps not mounted under /
_PWA_SCRIPT_PREFIX = get_script_prefix()

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates',
                                               'serviceworker.js'))
# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'MyApp')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'My Progressive Web App')
PWA_APP_ROOT_URL = resolve_url(getattr(settings, 'PWA_APP_ROOT_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_BACKGROUND_COLOR = getattr(settings, 'PWA_APP_BACKGROUND_COLOR', '#fff')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_SCOPE = resolve_url(getattr(settings, 'PWA_APP_SCOPE', _PWA_SCRIPT_PREFIX))
PWA_APP_DEBUG_MODE = getattr(settings, 'PWA_APP_DEBUG_MODE', True)
PWA_APP_ORIENTATION = getattr(settings, 'PWA_APP_ORIENTATION', 'any')
PWA_APP_START_URL = resolve_url(getattr(settings, 'PWA_APP_START_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_FETCH_URL = resolve_url(getattr(settings, 'PWA_APP_FETCH_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_STATUS_BAR_COLOR = getattr(settings, 'PWA_APP_STATUS_BAR_COLOR', 'default')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    {
        'src': '/static/images/icons/icon-72x72.png',
        'size': '72x72'
    },
    {
        'src': '/static/images/icons/icon-96x96.png',
        'size': '96x96'
    },
    {
        'src': '/static/images/icons/icon-128x128.png',
        'size': '128x128'
    },
    {
        'src': '/static/images/icons/icon-144x144.png',
        'size': '144x144'
    },
    {
        'src': '/static/images/icons/icon-152x152.png',
        'size': '152x152'
    },
    {
        'src': '/static/images/icons/icon-192x192.png',
        'size': '192x192'
    },
    {
        'src': '/static/images/icons/icon-384x384.png',
        'size': '384x384'
    },
    {
        'src': '/static/images/icons/icon-512x512.png',
        'size': '512x512'
    }
])

PWA_APP_DIR = getattr(settings, 'PWA_APP_DIR', 'auto')
PWA_APP_LANG = getattr(settings, 'PWA_APP_LANG', 'en-US')

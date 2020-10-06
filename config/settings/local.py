# from .base import *  # noqa
# from .base import env

# # GENERAL
# # ------------------------------------------------------------------------------
# DEBUG = True
# SECRET_KEY = env("DJANGO_SECRET_KEY", default="!!!SET DJANGO_SECRET_KEY!!!",)
# ALLOWED_HOSTS = ["*"]
# # STATIC
# # ------------------------------------------------------------------------------

# # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = "/static/"
# # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS

# # https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = str(BASE_DIR / "staticfiles")

# STATICFILES_DIRS = [str(APPS_DIR / "static")]
# # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
# STATICFILES_FINDERS = [
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# ]

# # CACHES
# # ------------------------------------------------------------------------------
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#         "LOCATION": "",
#     }
# }

# # EMAIL
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = env(
#     "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend",
# )
# # STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # WhiteNoise
# # ------------------------------------------------------------------------------
# # http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
# INSTALLED_APPS = [  # noqa: F405
#     "whitenoise.runserver_nostatic",
# ] + INSTALLED_APPS  # noqa: F405
# "django-debug-toolbar"
# # ------------------------------------------------------------------------------
# # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
# # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
# MIDDLEWARE += [  # noqa: F405
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]
# # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html
# DEBUG_TOOLBAR_PANELS = [
#     "ddt_request_history.panels.request_history.RequestHistoryPanel",
#     "debug_toolbar.panels.versions.VersionsPanel",
#     "debug_toolbar.panels.timer.TimerPanel",
#     "debug_toolbar.panels.settings.SettingsPanel",
#     "debug_toolbar.panels.headers.HeadersPanel",
#     "debug_toolbar.panels.request.RequestPanel",
#     "debug_toolbar.panels.sql.SQLPanel",
#     "debug_toolbar.panels.staticfiles.StaticFilesPanel",
#     "debug_toolbar.panels.templates.TemplatesPanel",
#     "debug_toolbar.panels.cache.CachePanel",
#     "debug_toolbar.panels.signals.SignalsPanel",
#     "debug_toolbar.panels.logging.LoggingPanel",
#     "debug_toolbar.panels.redirects.RedirectsPanel",
#     "debug_toolbar.panels.profiling.ProfilingPanel",
# ]
# # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
# DEBUG_TOOLBAR_CONFIG = {
#     "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
#     "SHOW_TEMPLATE_CONTEXT": True,
# }
# # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
# INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# # django-extensions
# # ------------------------------------------------------------------------------
# # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
# INSTALLED_APPS += ["django_extensions"]  # noqa: F405

# # Your stuff...
# # ------------------------------------------------------------------------------


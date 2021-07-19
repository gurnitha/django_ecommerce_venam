# apps/core/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.core.views import homepage

# appname
app_name = 'core'

urlpatterns = [
    path('', homepage, name='homepage'),
]

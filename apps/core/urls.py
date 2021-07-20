# apps/core/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.core.views import home

# appname
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
]

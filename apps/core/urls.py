# apps/core/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.core.views import home, category

# appname
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('categories/', category, name='categories'),
]

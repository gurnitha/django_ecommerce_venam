# apps/core/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage views
def homepage(request):
	return render(request, 'core/index.html')
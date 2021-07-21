# apps/core/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.core.models import Category

# Create your views here.

# Home page views
def home(request):
	return render(request, 'core/index.html')

# Categories page views
def category(request):
	data = Category.objects.all().order_by('-id')
	context = {'data':data}
	return render(request, 'core/category_list.html', context)
# apps/core/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.core.models import Category, Brand

# Create your views here.

# Home page views
def home(request):
	return render(request, 'core/index.html')

# Categories page views
def category_list(request):
	data = Category.objects.all().order_by('-id')
	context = {'data':data}
	return render(request, 'core/category_list.html', context)


# Brand
# Categories page views
def brand_list(request):
	data = Brand.objects.all().order_by('-id')
	print(data)
	context = {'data':data}
	return render(request, 'core/brand_list.html', context)





























































# apps/core/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.core.models import Category, Brand, Product

# Create your views here.

# Home page views
def home(request):
	return render(request, 'core/index.html')

# Category List views
def category_list(request):
	data = Category.objects.all().order_by('-id')
	context = {'data':data}
	return render(request, 'core/category_list.html', context)

# Brand List views
def brand_list(request):
	data = Brand.objects.all().order_by('-id')
	# print(data)
	context = {'data':data}
	return render(request, 'core/brand_list.html', context)

# Product List views
def product_list(request):
	data=Product.objects.all().order_by('-id')
	context = {'data':data}
	return render(request,'core/product_list.html',)



























































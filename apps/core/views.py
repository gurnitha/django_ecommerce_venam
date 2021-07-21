# apps/core/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.core.models import Banner, Category, Brand, Product, ProductAttribute

# Create your views here.

# Home page views
def home(request):
	banners = Banner.objects.all().order_by('-id')
	data = Product.objects.filter(is_featured=True).order_by('-id')
	print(banners)
	context = {
		'data':data,
		'banners':banners
	}
	return render(request, 'core/index.html', context)

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
	# Get all products and order by LIFO
	data = Product.objects.all().order_by('-id')
	# Get product based on category
	cats   = Product.objects.distinct().values(
				'category__title', 'category__id')
	brands = Product.objects.distinct().values(
				'brand__title', 'brand__id')
	colors = ProductAttribute.objects.distinct().values(
				'color__title', 'color__id', 'color__color_code')
	sizes  = ProductAttribute.objects.distinct().values(
				'size__title', 'size__id')
	print(sizes)
	context = {
		'data':data,
		'cats':cats,
		'brands':brands,
		'sizes':sizes,
		'colors':colors
	}
	return render(request,'core/product_list.html', context)


# Product List According to Category
def category_product_list(request,cat_id):
	category = Category.objects.get(id=cat_id)
	data     = Product.objects.filter(category=category).order_by('-id')
	cats   = Product.objects.distinct().values(
				'category__title', 'category__id')
	brands = Product.objects.distinct().values(
				'brand__title', 'brand__id')
	colors = ProductAttribute.objects.distinct().values(
				'color__title', 'color__id', 'color__color_code')
	sizes  = ProductAttribute.objects.distinct().values(
				'size__title', 'size__id')	
	context = {
		'data':data,
		'cats':cats,
		'brands':brands,
		'sizes':sizes,
		'colors':colors
	}
	return render(request,'core/category_product_list.html', context)
























































# apps/core/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.core.views import (
        home, category_list, 
        brand_list, product_list, 
        category_product_list,brand_product_list)

# appname
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('category-list/', 
                        category_list, name='category-list'),
    path('brand-list/', 
                        brand_list, name='brand-list'),
    path('product-list',
                        product_list,name='product-list'),
    path('category-product-list/<int:cat_id>',
                        category_product_list,name='category-product-list'),
    path('brand-product-list/<int:brand_id>',
                        brand_product_list,name='brand-product-list'),
]

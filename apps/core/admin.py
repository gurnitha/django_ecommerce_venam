# apps/core/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.core.models import (Banner, Category,
		Brand, Color, Size, 
		Product, ProductAttribute)

# Register your models here.
admin.site.register(Brand)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text',)
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','brand','status','is_featured')
    list_editable=('status','is_featured')
admin.site.register(Product,ProductAdmin)

# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)

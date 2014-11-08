from django.contrib import admin
from products.models import Product, ProductImage, ProductModel, Category

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductModelInline(admin.TabularInline):
    model = ProductModel

class ProductAdmin(admin.ModelAdmin):    
    inlines = [
        ProductImageInline,      
        ProductModelInline        
    ]
    prepopulated_fields = {
        'slug': ('title', ) 
    }

admin.site.register(Product, ProductAdmin)


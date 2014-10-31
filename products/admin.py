from django.contrib import admin
from products.models import Product, ProductImage, ProductModel, Category

admin.site.register(Product)
admin.site.register(Category)


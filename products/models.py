from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    description = models.TextField()


class Product(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    available = models.BooleanField(default=True)
    description = models.TextField()
    related = models.ManyToManyField("self")


class ProductModel(models.Model):
    product = models.ForeignKey(Product)
    sku = models.CharField(max_length=32, unique=True)
    model = models.CharField(max_length=32)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(blank=True, null=True, max_length=32)

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField()
    caption = models.TextField()


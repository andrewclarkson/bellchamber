from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    related = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self):
        return self.title

class ProductModel(models.Model):
    product = models.ForeignKey(Product)
    sku = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(blank=True, null=True, max_length=32)

    def __str__(self):
        return self.sku

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField()
    caption = models.TextField()

    def __str__(self):
        return self.image.name

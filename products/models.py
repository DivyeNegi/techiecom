from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique = True, null = True, blank = True)
    category_image = models.ImageField(upload_to="categories", height_field=None, width_field=None, max_length=None)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.category_name
    
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique = True, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")

class Storage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="storage_variants")
    storage_title = models.CharField(max_length=10)
    price_increase = models.IntegerField()

    def __str__(self) -> str:
        return self.storage_title+'//'+self.product.product_name

class Color(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="color_variants")
    color_title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.color_title+'//'+self.product.product_name

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from decimal import Decimal
from django.db.models import DecimalField
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)
    icon = models.ImageField(verbose_name="Иконка", upload_to='images/', null=True, blank=True)
    slug = models.SlugField(verbose_name="Слаг", max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    sub_categories = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True)
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(verbose_name="Слаг", max_length=100, unique=True, blank=True)
    main_image = models.ImageField(verbose_name="Изображение", upload_to='products/main/')
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=10)
    color = models.CharField(verbose_name="Цвет", max_length=50, null=True, blank=True)
    code = models.CharField(verbose_name="код товара", max_length=10, null=True, blank=True)
    article = models.IntegerField(verbose_name="Артикул", null=True)
    discount = models.PositiveIntegerField(verbose_name="Процент скидки", null=True)
    price_with_discount = models.DecimalField(verbose_name="Цена со скидкой", max_digits=10, decimal_places=2, null=True, blank=True)
    amount = models.PositiveIntegerField(verbose_name="количевство", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    hit = models.BooleanField(default=False)
    promotion = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.discount:
            self.price_with_discount = self.price * (1 - Decimal(self.discount) / Decimal(100))
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/extra/")

class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='product_sizes', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.size.name} ({self.stock} in stock) for {self.product.name}"




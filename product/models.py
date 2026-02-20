from django.contrib.auth.models import AbstractUser, User
from django.db import models
from decimal import Decimal
from ckeditor.fields import RichTextField
from django.db.models import DecimalField
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)
    icon = models.ImageField(verbose_name="Иконка", upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sub_categories = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True)
    name = models.CharField(verbose_name="Название", max_length=100)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=10)
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
        self.price_with_discount = self.price * (1 - Decimal(self.discount) / Decimal(100))
        super().save(*args, **kwargs)


class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    text = RichTextField("Описание")


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product")



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
            ("new", "New"),
            ("paid", "Paid"),
            ("shipped", "Shipped"),
            ("completed", "Completed"),
            ("canceled", "Canceled"),
        ], default="new"
    )

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def get_total_price(self):
        return self.quantity * self.price


from django.db import models
from decimal import Decimal
from ckeditor.fields import RichTextField
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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.price_with_discount = self.price * (1 - Decimal(self.discount) / Decimal(100))
        super().save(*args, **kwargs)

class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    text = RichTextField("Описание")


class ProductImage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    image = models.ImageField("фотография", upload_to="product")



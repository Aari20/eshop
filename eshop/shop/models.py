from django.db import models

# Create your models here.
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class SizeShoes(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class SizeShirt(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class SizePants(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    size_shoes = models.ManyToManyField(SizeShoes, blank=True)
    size_shirt = models.ManyToManyField(SizeShirt, blank=True)
    size_pants = models.ManyToManyField(SizePants, blank=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        #index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

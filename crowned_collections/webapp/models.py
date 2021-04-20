from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False)
    image_url = models.CharField(max_length=2083, null=False)
    stock = models.IntegerField(null=True)
    price = models.IntegerField(null=False)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("webapp:order", kwargs={
            'slug': self.slug,
        })

    def get_product_view(self):
        return reverse("webapp:product_page", kwargs={
            'slug': self.slug,
        })

    def add_to_cart_url(self):
        return reverse("webapp:add-to-cart", kwargs={
            'slug': self.slug,
        })


class Order(models.Model):
    product_name = models.CharField(max_length=100, null=False)
    FullName = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=100, null=False)



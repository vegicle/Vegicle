from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=200, null=True)
    slider_image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Varients(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='varients')
    quantity = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, help_text='The price of product')

    def __str__(self):
        return self.product.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

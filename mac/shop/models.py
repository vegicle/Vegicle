from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import ModelForm


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
    quantity_number = models.CharField(max_length=70, default="")
    quantity_measure = models.CharField(max_length=50, default='gms', null=True, help_text='gms, kg, etc.')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

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


class Instruction(models.Model):
    title = models.CharField(default="", max_length=200)
    instruction_message = models.CharField(blank=True, max_length=1000)
    min_coast = models.DecimalField(default=0, decimal_places=2, max_digits=10, help_text='Minimal coast of something')

    def __str__(self):
        return self.title


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=5000, blank=True)
    firstName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=110, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=50, blank=True)

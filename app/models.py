from django.db import models
from django.utils.html import format_html
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    def image_tag(self):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.name}'

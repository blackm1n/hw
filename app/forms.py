from django import forms
from .models import Product

class EditProductImage(forms.Form):
    pk = forms.ChoiceField(choices=[(product.id, product.name) for product in Product.objects.all()])
    image = forms.ImageField()
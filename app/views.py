from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product
from datetime import datetime, timedelta
from .forms import EditProductImage

def my_view(request):
    return render(request, "app/index.html", {})

def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'app/client_orders.html', {'name': client.name, 'orders': orders})

def client_products(request, length, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    products = []
    for order in orders:
        products += order.products.all()
    products = list(set(products))
    match length:
        case 'week': days = 7
        case 'month': days = 30
        case 'year': days = 365
        case _:
            return HttpResponseNotFound('invalid length, must be week, month or year')
    products = [product for product in products if product.date_created.replace(tzinfo=None) > datetime.now().replace(tzinfo=None) - timedelta(days=days)]
    return render(request, 'app/client_products.html', {'name': client.name, 'products': reversed(sorted(products, key=lambda product: product.date_created))})

def product_image(request):
    if request.method == 'POST':
        form = EditProductImage(request.POST, request.FILES)
        if form.is_valid():
            pk = form.cleaned_data['pk']
            product = Product.objects.filter(pk=pk).first()
            image = form.cleaned_data['image']
            product.image = image
            product.save()
    else:
        form = EditProductImage()
    return render(request, 'app/product_image.html', {'form': form})
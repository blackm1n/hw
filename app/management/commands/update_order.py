from django.core.management.base import BaseCommand
from ...models import Order, Product
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)
        parser.add_argument('action', type=str)
        parser.add_argument('product_id', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        action = kwargs['action']
        product_id = kwargs['product_id']
        order = Order.objects.filter(pk=pk).first()
        product = Product.objects.filter(pk=product_id).first()
        match action:
            case 'add':
                order.products.add(product)
                order.total_price += product.price
            case 'remove':
                order.products.remove(product)
                order.total_price -= product.price
        order.save()
        self.stdout.write(f'{order}')
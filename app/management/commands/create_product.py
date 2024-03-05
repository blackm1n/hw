from django.core.management.base import BaseCommand
from ...models import Product

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=int)
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        price = kwargs['price']
        count = kwargs['count']
        product = Product(name=name, description=description, price=price, count=count)
        product.save()
        self.stdout.write(f'{product}')
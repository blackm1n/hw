from django.core.management.base import BaseCommand
from ...models import Product

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f'{products}')
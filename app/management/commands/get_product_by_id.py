from django.core.management.base import BaseCommand
from ...models import Product

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
from django.core.management.base import BaseCommand
from ...models import Product
from datetime import datetime
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)
        parser.add_argument('key', type=str)
        parser.add_argument('data', type=str)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        key = kwargs['key']
        data = kwargs['data']
        product = Product.objects.filter(pk=pk).first()
        match key:
            case 'name': product.name = data
            case 'description': product.description = data
            case 'price': product.price = float(data)
            case 'count': product.count = int(data)
            case 'datetime': product.date_created = datetime.strptime(data, '%m-%d-%yt%H:%M:%S').replace(tzinfo=None)
        product.save()
        self.stdout.write(f'{product}')
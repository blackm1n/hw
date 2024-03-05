from django.core.management.base import BaseCommand
from ...models import Order

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'Done')
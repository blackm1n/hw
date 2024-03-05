from django.core.management.base import BaseCommand
from ...models import Order

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        self.stdout.write(f'{orders}')
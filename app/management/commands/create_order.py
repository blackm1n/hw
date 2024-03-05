from django.core.management.base import BaseCommand
from ...models import Order, Client

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        client = Client.objects.filter(pk=client_id).first()
        order = Order(client=client, total_price=0)
        order.save()
        self.stdout.write(f'{order}')
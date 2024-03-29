from django.core.management.base import BaseCommand
from ...models import Client

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')
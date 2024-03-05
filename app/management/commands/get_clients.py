from django.core.management.base import BaseCommand
from ...models import Client

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
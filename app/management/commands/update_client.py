from django.core.management.base import BaseCommand
from ...models import Client
from phonenumbers import parse, format_number, PhoneNumberFormat

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)
        parser.add_argument('key', type=str)
        parser.add_argument('data', type=str)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        key = kwargs['key']
        data = kwargs['data']
        client = Client.objects.filter(pk=pk).first()
        match key:
            case 'name': client.name = data
            case 'email': client.email = data
            case 'phone': client.phone = format_number(parse(data, "RU"), PhoneNumberFormat.NATIONAL)
            case 'address': client.address = data
        client.save()
        self.stdout.write(f'{client}')
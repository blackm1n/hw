from django.core.management.base import BaseCommand
from ...models import Client
from phonenumbers import parse, format_number, PhoneNumberFormat

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        phone = format_number(parse(kwargs['phone'], "RU"), PhoneNumberFormat.NATIONAL)
        address = kwargs['address']
        client = Client(name=name, email=email, phone=phone, address=address)
        client.save()
        self.stdout.write(f'{client}')
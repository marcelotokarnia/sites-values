# coding: utf-8
from django.core.management.base import BaseCommand
from datetime import date
from core.models import Site, Value

sites = [
    {'name': 'Demo Site', 'values': [
        {'pk': 1, 'date': date(2015, 2, 1), 'a': 12, 'b': 16},
        {'pk': 2, 'date': date(2015, 2, 3), 'a': 20, 'b': 100},
        {'pk': 3, 'date': date(2015, 2, 10), 'a': 20, 'b': 80},
    ]},
    {'name': 'ABC Site', 'values': [

    ]},
    {'name': 'XYZ Site', 'values': [

    ]}
]

class Command(BaseCommand):
    help = "Usage Report on Given Day"

    def handle(self, *args, **options):
        for site in sites:
            site_entity, _ = Site.objects.get_or_create(name=site['name'])
            for value in site['values']:
                Value.objects.get_or_create(pk=value['pk'], defaults={
                    'site': site_entity,
                    **value
                })
# coding: utf-8
import sys
import traceback
import datetime
from django.core.management.base import BaseCommand
from core.models import IpUsage


class Command(BaseCommand):
    help = "Usage Report on Given Day"

    def add_arguments(self, parser):
        parser.add_argument('--date')

    def handle(self, *args, **options):
        date = datetime.datetime.strptime(options['date'], '%Y-%m-%d').date()
        ip_usages = IpUsage.objects.filter(date=date)
        with open('%s-ipusage-%s.csv' % (datetime.datetime.now().toordinal(), date), 'w') as f:
          f.write('IP,USAGE\n')
          for ip in ip_usages:
            f.write('%s,%s\n' % (ip.ip, ip.usage))
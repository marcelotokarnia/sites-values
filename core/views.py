from django.shortcuts import render
from core.serializers import SitesSerializer
from core.models import Site
from rest_framework import viewsets
from django.http import JsonResponse
from utils.model_utils import mean
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def sites_summary(request):
    q = Site.objects.raw('''
        SELECT s.id AS id, s.name AS name, v.sum_a AS sum_a, v.sum_b AS sum_b
        FROM core_site s, (
            SELECT SUM(a) AS sum_a, SUM(b) AS sum_b, site_id FROM core_value GROUP BY site_id
        ) v
        WHERE s.id = v.site_id
    ''')
    return JsonResponse([
        {'id': s.id, 'name': s.name, 'sum': {'a': s.sum_a, 'b': s.sum_b}} for s in q
    ], safe=False)


@csrf_exempt
def sites_summary_average(request):
    q = Site.objects.all()
    return JsonResponse([
        {
            'id': s.id,
            'name': s.name,
            'average': {
                'a': mean(s.values.values_list('a', flat=True)),
                'b': mean(s.values.values_list('b', flat=True)),
            }
        } for s in q
    ], safe=False)


class SitesViewSet(viewsets.ModelViewSet):
    serializer_class = SitesSerializer

    def get_queryset(self):
        return Site.objects.all()


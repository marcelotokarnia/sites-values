from django.shortcuts import render
from core.serializers import SitesSerializer
from core.models import Site
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def sites_summary(request):
    return JsonResponse([
        {'id': 1, 'name': 'Demo Site', 'sum': {'a': 52, 'b': 196}},
        {'id': 2, 'name': 'ABC Site', 'sum': {'a': 5, 'b': 15}},
        {'id': 3, 'name': 'XYZ Site', 'sum': {'a': 10, 'b': 30}}
    ], safe=False)


@csrf_exempt
def sites_summary_average(request):
    return JsonResponse([
        {'id': 1, 'name': 'Demo Site', 'average': {'a': 17.33, 'b': 65.33}},
        {'id': 2, 'name': 'ABC Site', 'average': {'a': 5, 'b': 15}},
        {'id': 3, 'name': 'XYZ Site', 'average': {'a': 5, 'b': 15}}
    ], safe=False)


class SitesViewSet(viewsets.ModelViewSet):
    serializer_class = SitesSerializer

    def get_queryset(self):
        return Site.objects.all()


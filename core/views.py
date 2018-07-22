from django.shortcuts import render
from core.serializers import SitesSerializer
from core.models import Site
from rest_framework import viewsets
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def sites_summary(request):
    return JsonResponse({'foo': 'bar'})


def sites_summary_average(request):
    return JsonResponse({'foo': 'bar'})


class SitesViewSet(viewsets.ModelViewSet):
    serializer_class = SitesSerializer

    def get_queryset(self):
        return Site.objects.all()


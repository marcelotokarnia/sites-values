from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from core.views import index, SitesViewSet, sites_summary, sites_summary_average
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sites', SitesViewSet, base_name='sites')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    path('api/sites-summary-average', sites_summary_average),
    path('api/sites-summary', sites_summary),
    url(r'', index),
]

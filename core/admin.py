from django.contrib import admin
from core.models import IpUsage

@admin.register(IpUsage)
class IpUsageAdmin(admin.ModelAdmin):
  pass

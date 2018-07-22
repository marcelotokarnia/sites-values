from django.contrib import admin
from core.models import Site, Value
from utils.admin_utils import RawIdAdminModel


class ValueAdmin(admin.TabularInline):
    model = Value
    extra = 0


class SiteAdmin(RawIdAdminModel):
    inlines = (ValueAdmin, )


admin.site.register(Site, SiteAdmin)

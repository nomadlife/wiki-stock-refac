from django.contrib import admin

# Register your models here.
from .models import Company

# admin.site.register(Company)
# admin.site.site_header = "UMSRA Admin"
# admin.site.site_title = "UMSRA Admin Portal" # ?? not work
# admin.site.index_title = "Welcome to UMSRA Researcher Portal"

from django.contrib.admin import AdminSite
import csv
from django.http import HttpResponse

class SomeModelAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_as_csv.short_description = "Export Selected"



class EventAdminSite(AdminSite):
    site_header = "Stock Site Admin"
    index_title = "Welcome to Stock Site Portal"
    
event_admin_site = EventAdminSite(name='event_admin')
event_admin_site.register(Company, SomeModelAdmin)



...


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
from django.urls import path
from django.http import HttpResponseRedirect

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
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('immortal/', self.set_immortal),
            path('mortal/', self.set_mortal),
        ]
        return my_urls + urls

    def set_immortal(self, request):
        self.model.objects.all().update(ticker_code='999999')
        self.message_user(request, "All heroes are now immortal")
        return HttpResponseRedirect("../")

    def set_mortal(self, request):
        self.model.objects.all().update(ticker_code='111111')
        self.message_user(request, "All heroes are now mortal")
        return HttpResponseRedirect("../")

class EventAdminSite(AdminSite):
    site_header = "Stock Site Admin"
    index_title = "Welcome to Stock Site Portal"
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    change_list_template = "stock/temp_changelist.html"
    
event_admin_site = EventAdminSite(name='event_admin')
event_admin_site.register(Company, SomeModelAdmin)




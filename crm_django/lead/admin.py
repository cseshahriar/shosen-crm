from django.contrib import admin
from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    """ lead admin """
    list_display = ('contact_person', 'email', 'phone')
    list_display_links = ('contact_person',)
    

admin.site.register(Lead, LeadAdmin)
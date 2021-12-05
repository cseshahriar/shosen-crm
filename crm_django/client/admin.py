from django.contrib import admin

from .models import Client, Note

admin.site.register(Client)
admin.site.register(Note)
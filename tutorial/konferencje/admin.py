from django.contrib import admin

# Register your models here.

from .models import Conference, Abstract

class AbstractInline(admin.TabularInline):
    model = Abstract



class ConferenceAdmin(admin.ModelAdmin):
    model = Conference

    inlines = [AbstractInline]

admin.site.register(Abstract)
admin.site.register(Conference,ConferenceAdmin)

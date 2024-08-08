from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_time')
    search_fields = ('title', 'location')
    list_filter = ('date_time',)

admin.site.register(Event, EventAdmin)

from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_time', 'end_time')
    search_fields = ('title', 'location', 'organizer')
    list_filter = ('start_time', 'end_time')

admin.site.register(Event, EventAdmin)

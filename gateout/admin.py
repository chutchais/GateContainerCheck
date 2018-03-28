from django.contrib import admin

# Register your models here.
from .models import vessel,voy,booking,container,container_images

class VesselAdmin(admin.ModelAdmin):
    search_fields = ['name','code','description']
    list_filter = ['name','code']
    list_display = ('name','code','description','created_date','user')
    fieldsets = [
        (None,               {'fields': ['name','code','description','user']}),
    ]
admin.site.register(vessel,VesselAdmin)


class VoyAdmin(admin.ModelAdmin):
    search_fields = ['voy','vessel','description']
    list_filter = ['voy','vessel']
    list_display = ('voy','vessel','description','created_date','user')
    fieldsets = [
        (None,               {'fields': ['voy','vessel','description','user']}),
    ]
admin.site.register(voy,VoyAdmin)


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['booking','line','voy','description']
    list_filter = ['line']
    list_display = ('booking','line','voy','description','created_date','user')
    fieldsets = [
        (None,               {'fields': ['booking','line','voy','description','user']}),
    ]
admin.site.register(booking,BookingAdmin)


admin.site.register(container)
admin.site.register(container_images)
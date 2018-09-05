from django.contrib import admin

# Register your models here.
from .models import Machine

class MachineAdmin(admin.ModelAdmin):
    search_fields = ['name','ip','description']
    list_filter = ['machine_type']
    list_display = ('name','ip','description','last_loggin_date')
    fieldsets = [
        (None,               {'fields': ['name','ip','machine_type','description']}),
    ]
admin.site.register(Machine,MachineAdmin)
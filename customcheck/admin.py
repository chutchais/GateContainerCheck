from django.contrib import admin

# Register your models here.
from .models import container

class ContainerAdmin(admin.ModelAdmin):
    search_fields = ['container_no','description']
    list_filter = ['created_date']
    list_display = ('container_no','description','created_date','user')
    fieldsets = [
        (None,               {'fields': ['container_no','description','user']}),
    ]
admin.site.register(container,ContainerAdmin)

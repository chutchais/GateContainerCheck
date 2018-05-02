from django.contrib import admin

# Register your models here.
from .models import container,reject

class ContainerAdmin(admin.ModelAdmin):
    search_fields = ['container_no','description']
    list_filter = ['created_date']
    list_display = ('container_no','description','created_date')
    fieldsets = [
        (None,               {'fields': ['container_no','description']}),
    ]
admin.site.register(container,ContainerAdmin)


class RejectAdmin(admin.ModelAdmin):
    search_fields = ['container_no','description']
    list_filter = ['created_date']
    list_display = ('container_no','no_shore','no_paid',
    			'no_customs','no_vgm','late_gate','other','created_date')
    fieldsets = [
        (None,               {'fields': ['container_no','no_shore','no_paid',
    			'no_customs','no_vgm','late_gate','other','description',]}),
    ]
admin.site.register(reject,RejectAdmin)
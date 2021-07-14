from django.contrib import admin
from .models import Department,Doctor,Patient

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Doctor,DoctorAdmin)

admin.site.register(Patient)
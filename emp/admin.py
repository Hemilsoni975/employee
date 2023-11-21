from django.contrib import admin

# Register your models here.

from emp.models import Employee, Role, Department

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
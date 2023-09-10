from django.contrib import admin
from myapp.models import Company,Employee
'''sandeep\12345'''
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)
    list_filter=('type',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone')
    search_fields=('name',)
    list_filter=('email',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
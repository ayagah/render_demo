from django.contrib import admin

# Register your models here.
from.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=("name","roll_number","date_registered")
    

admin.site.register(Student,StudentAdmin)

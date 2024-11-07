from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Departement)
admin.site.register(Student)
admin.site.register(Subject)


#  create a class to show the data in admin pannel in custom form
class SUbjectMarksAdmin(admin.ModelAdmin):
    list_display =['student','subject','marks']
admin.site.register(SubjectMarks,SUbjectMarksAdmin)

from django.contrib import admin

from .models import Student, Group #Add Group after comma here
# Register your models here.
admin.site.register(Student)
admin.site.register(Group)

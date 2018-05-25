from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)

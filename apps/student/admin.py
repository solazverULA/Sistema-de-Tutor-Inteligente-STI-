from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    pass


class ThemeAdmin(admin.ModelAdmin):
    pass


class LearningThemeAdmin(admin.ModelAdmin):
    pass


class ProblemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(LearningTheme, LearningThemeAdmin)
admin.site.register(Problem, ProblemAdmin)

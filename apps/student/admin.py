from django.contrib import admin
from .models import *


class ProgressInline(admin.TabularInline):
    model = Progress

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class StudentAdmin(admin.ModelAdmin):
    inlines = [ProgressInline, ]


class ThemeAdmin(admin.ModelAdmin):
    pass


class LearningThemeAdmin(admin.ModelAdmin):
    pass


class DifficultInline(admin.TabularInline):
    model = Difficult

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class ProblemAdmin(admin.ModelAdmin):
    inlines = [DifficultInline,]


admin.site.register(Student, StudentAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(LearningTheme, LearningThemeAdmin)
admin.site.register(Problem, ProblemAdmin)
# admin.site.register(Progress, ProgressAdmin)
# admin.site.register(Difficult, DifficultAdmin)

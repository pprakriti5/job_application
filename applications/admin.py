from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'expertise', 'cv')
    list_filter = ('expertise',)
    ordering = ('experience',)

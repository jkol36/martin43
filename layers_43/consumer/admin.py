from django.contrib import admin
from models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	fields = ['user', 'is_submitted', 'budget', 'description', 'deadline', 'photo']

admin.site.register(Project, ProjectAdmin)

from django.contrib import admin
from models import Project, ProjectUpdate, ProjectUpdateItem

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	fields = ['user', 'is_submitted', 'budget', 'description', 'deadline']

class ProjectUpdateAdmin(admin.ModelAdmin):
	fields = ['project', 'user', 'update_type', 'message', 'amount_required', 'current_status', 'name']

class ProjectUpdateItemAdmin(admin.ModelAdmin):
	fields =['photo', 'update']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUpdate, ProjectUpdateAdmin)
admin.site.register(ProjectUpdateItem, ProjectUpdateItemAdmin)

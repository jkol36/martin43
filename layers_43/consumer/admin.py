from django.contrib import admin
from models import Project, ProjectUpdate, ProjectUpdateItem
from layers_43.messaging.models import Message

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	fields = ['user', 'is_submitted', 'budget', 'title', 'description', 'deadline']

class ProjectUpdateAdmin(admin.ModelAdmin):
	fields = ['project', 'user', 'update_type', 'message', 'amount_required', 'current_status', 'name']

class ProjectUpdateItemAdmin(admin.ModelAdmin):
	fields =['photo', 'update']
class messageAdmin(admin.ModelAdmin):
	list_display = ['text', 'recipient', 'sender']

admin.site.register(Message, messageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUpdate, ProjectUpdateAdmin)
admin.site.register(ProjectUpdateItem, ProjectUpdateItemAdmin)

from django.contrib import admin
from .models import Task, Project

class ProjectAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'description', 'start_date', ]
   search_fields =['name']
   list_editable = [ 'start_date',]
   list_display_links = ['id', 'name']

admin.site.register(Project, ProjectAdmin)

# Create Admin view of tables
class TaskAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'project', 'owner', 'title', 'details', 'due_date','priority', 'status', ]
    search_fields =['title']
    list_editable = ['priority', 'status', 'due_date']
    list_filter = ['project', 'due_date', 'priority', 'status',]
    list_display_links = ['id', 'title']
    list_per_page = 8

admin.site.register(Task, TaskAdmin)

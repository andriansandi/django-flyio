from django.contrib import admin

# Model
from .models import *

# Remove sidebar
admin.site.enable_nav_sidebar = False

# Todo
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):    
    list_display = ('todo',)

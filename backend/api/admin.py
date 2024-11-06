"""This module handles the admin functionalities."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """This class is responsible for managing admin tasks."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)

from django.contrib import admin

# Register your models here.
from todolist.models import Task
admin.site.register(Task)
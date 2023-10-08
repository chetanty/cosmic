from django.contrib import admin
from .models import Project, SkillSet, SavedProject

# Register your models here.
admin.site.register(Project)
admin.site.register(SkillSet)
admin.site.register(SavedProject)
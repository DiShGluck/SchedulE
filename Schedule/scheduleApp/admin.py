from django.contrib import admin
from .models import Group, Teacher, Subject, Schedule

admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Schedule)
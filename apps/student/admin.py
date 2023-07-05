from django.contrib import admin

from apps.student.models import Student, University


admin.site.register(University)
admin.site.register(Student)

from django.contrib import admin

from school.models import Classroom, Course, DayOfTheWeek

# Register your models here.

admin.site.register(DayOfTheWeek)
admin.site.register(Classroom)
admin.site.register(Course)
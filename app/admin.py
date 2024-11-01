from django.contrib import admin

from .models import Course, Lesson, Comment, Rating

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Rating)

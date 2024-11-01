from rest_framework.pagination import CursorPagination

class CoursePagination(CursorPagination):
    ordering = '-created_at'

class LessonPagination(CursorPagination):
    ordering = '-created_at'

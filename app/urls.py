from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, CommentViewSet, RatingViewSet


""" DefaultRouter'dan foydalanish ViewSet'lar 
    uchun avtomatik marshrutlarni yaratadi.
    Router /courses/, /lessons/, /comments/, 
    va /ratings/ ko'rinishida avtomatik ravishda hosil qiladi. """

app_name = 'app'

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)

""" Router orqali hosil 
    bo'lgan URL'larni 
    umumiy URL'lar 
    ro'yxatiga qo'shish """
urlpatterns = [
    path('', include(router.urls)),
]

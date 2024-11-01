from rest_framework import viewsets, permissions, filters
from .pagination import CoursePagination, LessonPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Course, Lesson, Comment, Rating
from .serializers import CourseSerializer, LessonSerializer, CommentSerializer, RatingSerializer
from .permissions import IsAdminOrReadOnly

class CourseViewSet(viewsets.ModelViewSet):
    """ Kurslarni boshqarish uchun ViewSet,
    faqat autentifikatsiyadan o'tgan foydalanuvchilarga
    CRUD operatsiyalarni bajarish, qidirish va
    tartiblash imkoniyatini beradi. """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CoursePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']

class LessonViewSet(viewsets.ModelViewSet):
    """ Darslarni boshqarish uchun ViewSet,
    faqat autentifikatsiyadan o'tgan
    foydalanuvchilarga CRUD
    operatsiyalarni bajarish,
    qidirish va tartiblash imkoniyatini
    beradi. """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LessonPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        """ Darslarga yoqtirish
        yoki yoqtirmaslik
        bahosini berish uchun custom action. """
        lesson = self.get_object()
        liked = request.data.get('liked')
        rating, acreated = Rating.objects.update_or_create(
            user=request.user, lesson=lesson,
            defaults={'liked': liked}
        )
        return Response({'status': 'rated'})

class CommentViewSet(viewsets.ModelViewSet):
    """ Izohlarni boshqarish
        uchun ViewSet, autentifikatsiyadan
        o'tgan foydalanuvchilarga
        yozish va barcha foydalanuvchilarga
        o'qish imkoniyatini beradi. """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RatingViewSet(viewsets.ModelViewSet):
    """ Baholarni boshqarish uchun ViewSet,
        faqat autentifikatsiyadan o'tgan
        foydalanuvchilarga baholash imkoniyatini
        beradi. """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

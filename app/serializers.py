from rest_framework import serializers
from .models import Course, Lesson, Comment, Rating

class CourseSerializer(serializers.ModelSerializer):
    """ Kurs ma'lumotlarini seriyalizatsiya qilish
        uchun serializer. Bu serializer kursning
        asosiy maydonlarini oladi:
        id, name, description va created_at. """
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'created_at']

class LessonSerializer(serializers.ModelSerializer):
    """ Dars ma'lumotlarini seriyalizatsiya
        qilish uchun serializer.
        Darsga tegishli kurs, nomi, video,
        yaratilgan sanasi va darsning umumiy
        reytinglarini qaytaradi. """
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'name', 'video', 'created_at', 'ratings']

    def get_ratings(self, obj):
        """ Darsga berilgan baholarni sanaydi,
            qaysi foydalanuvchilarga yoqqan va
            yoqmaganligini qaytaradi. """
        return {
            'likes': obj.ratings.filter(liked=True).count(),
            'dislikes': obj.ratings.filter(liked=False).count()
        }

class CommentSerializer(serializers.ModelSerializer):
    """ Darslarga qoldirilgan izohlarni
        seriyalizatsiya qilish uchun serializer.
        Izohga tegishli foydalanuvchi, dars,
        izoh matni va yaratilgan sanani oladi. """
    class Meta:
        model = Comment
        fields = ['id', 'lesson', 'user', 'text', 'created_at']

class RatingSerializer(serializers.ModelSerializer):
    """ Baholarni seriyalizatsiya qilish
    uchun serializer. Foydalanuvchi,
    dars va yoqtirish yoki yoqtirmaslikka
    qarab baho ma'lumotlarini oladi. """
    class Meta:
        model = Rating
        fields = ['id', 'lesson', 'user', 'liked']

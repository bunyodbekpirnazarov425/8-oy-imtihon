from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class CourseAnonThrottle(AnonRateThrottle):
    scope = 'course_anon_list'

class CourseUserThrottle(UserRateThrottle):
    scope = 'course_user_list'

class LessonAnonThrottle(AnonRateThrottle):
    scope = 'lesson_anon_list'

class LessonUserThrottle(UserRateThrottle):
    scope = 'lesson_user_list'

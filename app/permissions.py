from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Admin bo'lmagan foydalanuvchilar uchun faqat o'qish huquqini beradi.
    Admin bo'lgan foydalanuvchilar esa CRUD operatsiyalarni amalga oshira oladi.
    """
    def has_permission(self, request, view):
        # Agar foydalanuvchi faqat o'qish (GET, HEAD yoki OPTIONS) so'rovi jo'natsa, ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # Aks holda, faqat admin foydalanuvchilar uchun ruxsat beriladi
        return request.user and request.user.is_staff

from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone

class RegisteredMorethanThreeDaysUser(BasePermission):
    message ='가입 후 3일 이상 지난 사람만 사용가능'

    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and
                    request.user.join_data < (timezone.now() - timedelta(days=3)))
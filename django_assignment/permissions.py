from rest_framework.permissions import BasePermission
from datetime import timedelta, datetime
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status



class RegisteredMorethanThreeDaysUser(BasePermission):
    message ='가입 후 3일 이상 지난 사람만 사용가능'

    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and
                    request.user.join_data < (timezone.now() - timedelta(days=3)))


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        super().__init__(detail=detail, code=code)


class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    SAFE_METHODS = ('GET',)
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            response ={
                "detail":"서비스를 이용하기 위해 로그인하세요"
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNATHORIZED, detail=response)

        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True

        if user.is_authenticated and user.is_admin or \
            user.join_date < (datetime.now().date() - timedelta(days=7)):
            return True

        return False
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from blog.models import Article


class UserView(APIView): # CBV 방식
    permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        user = request.user.is_authenticated
        articles=Article.objects.filter(author_id=user)
        return render(request, 'index.html', {'article':articles})
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from blog.models import Article
from user.serializers import UserProfileSerializer, UserSignupSerializer

class UserView(APIView): # CBV 방식
    permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        return Response(UserSignupSerializer(request.user).data, status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"})
        else:
            return Response({"message":"가입실패"})


    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"})

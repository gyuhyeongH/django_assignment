from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from blog.models import Article
from user.serializer import UserProfileSerializer, UserSignupSerializer


class UserView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # 사용자 정보 조회
    def get(self, request):
        return Response({"message": "get method"})

    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    # 회원 정보 수정
    def put(self, request):
        return Response({"message": "put method!!"})

    # 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})

class UserAPIView(APIView):
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

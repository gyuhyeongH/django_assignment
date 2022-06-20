from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from django_assignment.permissions import RegisteredMorethanThreeDaysUser


class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [RegisteredMorethanThreeDaysUser]

    def get(self, request):
        user = request.user

        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles]

        return Response({"article_list": titles})

    def post(self, request):
        user = request.user
        title = request.data.get("title","")
        contents = request.data.get("contents","")
        categorys = request.data.get("category",[])

        if len(title) <= 5:
            return Response({"error":"5자이상 작성해야합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if len(contents) <= 20:
            return Response({"error":"20자이상 작성해야합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not categorys:
            return Response({"error":"카테고리가 작성되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        article = ArticleModel(
            user=user,
            title=title,
            contents=contents

        )
        article.save()
        article.category.add(*categorys)
        return Response({"message":"성공",}, status=status.HTTP_200_OK)
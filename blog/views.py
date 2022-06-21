from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from django_assignment.permissions import IsAdminOrIsAuthenticatedReadOnly
from blog.serializer import ArticleSerializer
from django.utils import timezone


class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    def get(self, request):
        user = request.user
        today = timezone
        articles = ArticleModel.objects.filter(
            exposure_start_date__lte=today,
            exposure_end_date__gte=today,
        ).order_by('-id')
        serializer = ArticleSerializer(articles, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        title = request.data.get("title","")
        contents = request.data.get("contents","")
        categorys = request.data.pop("category",[])

        if len(title) <= 5:
            return Response({"error":"5자이상 작성해야합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if len(contents) <= 20:
            return Response({"error":"20자이상 작성해야합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not categorys:
            return Response({"error":"카테고리가 작성되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        article = ArticleModel(
            user=user,
            **request.data
        )
        article.save()
        article.category.add(*categorys)
        return Response({"message":"성공",}, status=status.HTTP_200_OK)
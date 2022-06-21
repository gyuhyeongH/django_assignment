from rest_framework import serializers
from blog.models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["user","article","contents"]


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["user","title","category","contents"]
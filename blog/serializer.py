from rest_framework import serializers
from blog.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField

    def get_user(self, obj):
        return obj.username

    class Meta:
        model = Comment
        fields = ["user","article","contents"]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comment_set")

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = Article
        fields = ["user","title","category","comments"]

        
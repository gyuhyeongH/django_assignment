from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobby as HobbyModel
from blog.serializer import CommentSerializer,ArticleSerializer
from rest_framework import serializers


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields="__all__"

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileModel
        fields = ["fullname","email"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source="article_set")
    comments = CommentSerializer(many=True, source="comment_set")

    class Meta:
        model = UserModel
        fields = ["Username", "userprofile", "articles", "comments"]
from blog.models import Category as CastegoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobby as HobbyModel

from blog.serializers import ArticleSerializer


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

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    class UserProfileSerializer(serializers.ModelSerializer):

        class Meta:
            model = UserProfileModel
            fields = ["fullname","email"]


    class UserProfileSerializer(serializers.ModelSerializer):
        userprofile = UserProfileSerializer()
        articles = ArticleSerializer(many=True, source="article_set")
        comments = CommentSerializer(many=True, source="comment_set")
        class Meta:
            model = UserModel
            fields = ["Username","userprofile", "articles", "comments"]
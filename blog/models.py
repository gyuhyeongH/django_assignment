from django.db import models
from user.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)


class Article(models.Model):

    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문")


class Comment(models.Model):
    user = models.ForeignKey(
        'user.User', verbose_name='작성자', on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, verbose_name='게시글', on_delete=models.CASCADE)
    contents = models.TextField("본문")

    def __str__(self):
        return f"{self.article.title} / {self.contents}"
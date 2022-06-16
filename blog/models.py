from django.db import models
from user.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user')
    title = models.CharField(max_length=20, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    content = models.TextField(blank=True)


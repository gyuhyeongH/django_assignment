from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    title = models.CharField('제목', max_length=50)
    thumbnail = models.FileField("썸네일", upload_to ='product/')
    description = models.TextField("설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    modification_date = models.DateField("수정 일자", null=True)
    exposure_end_date = models.DateField("노출 종료 일자", default=timezone.now)
    price = models.IntegerField("가격", null=True)
    is_active = models.BooleanField("활성화 여부")


class Review(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.SET_NULL, null=True)
    contents = models.TextField("내용")
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    created = models.DateTimeField("등록일자", auto_now_add=True)


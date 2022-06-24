from rest_framework import serializers

from product.models import Product as ProductModel
from product.models import Review as ReviewModel
from datetime import datetime
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.fullname

    class Meta:
        model = ReviewModel
        fields = ['user', 'contents','created','rating']



class ProductSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()

    def get_review(self, obj):
        reviews = obj.review_set
        return {
            "last_review":ReviewSerializer(reviews.last()).data,
            "average_rating":reviews.agregate(Avg("rate"))
        }
    
    def validate(self, data):
        exposure_end_date = data.get("exposure_end_date")
        if exposure_end_date and exposure_end_date < datetime.now().date():
            raise serializers.ValidationError(
                    # custom validation error message
                    detail={"error": "노출 종료 일자가 지났습니다."},
                )

        # validation에 문제가 없을 경우 data return
        return data

    def create(self, validated_data):
        
        product = ProductModel(**validated_data)
        product.save()
        product.description = f"\n{product.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
        product.save()
        return product

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "description":
                value += f"\n{instance.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
            setattr(instance, key, value)
        instance.save()
        instance.description = f"{instance.modified.replace(microsecond=0, tzinfo=None)}에 수정되었습니다.\n"+instance.description
        instance.save()
        return instance

    class Meta:
        model = ProductModel
        fields = ['user', 'title','thumbnail','description',
        'created','review','modified','exposure_end_date','is_active','price']

        
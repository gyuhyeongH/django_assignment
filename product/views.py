from datetime import datetime
from itertools import product
from django.shortcuts import render
from product import serializer
from product.serializer import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
# Create your views here.
from datetime import datetime
from django.db.models import Q


class ProductView(APIView):
    def get(self, request):
        today = datetime.now()
        products = Product.objects.filter(
            Q(exposure_start_date__lte=today, exposure_end_date__gte=today,)|
            Q(user=request.user)
        )

        data = ProductSerializer(products, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id

        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

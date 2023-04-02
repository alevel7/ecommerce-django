from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing categories
    """

    queryset = Category.objects.all()

    # serializer = CategorySerializer
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response({"data": serializer.data})


class BrandViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing categories
    """

    queryset = Brand.objects.all()

    # serializer = CategorySerializer
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response({"data": serializer.data})


class ProductViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing categories
    """

    queryset = Product.objects.all()

    # serializer = CategorySerializer
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response({"data": serializer.data})

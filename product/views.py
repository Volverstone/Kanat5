from rest_framework import generics
from django.db.models import Avg, Count
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    ProductReviewsSerializer
)



class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.annotate(
            products_count=Count('products')
        )


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


# отзывы и средний рейтинг
class ProductReviewsAPIView(generics.ListAPIView):
    serializer_class = ProductReviewsSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            rating=Avg('reviews__stars')
        ).prefetch_related('reviews')


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

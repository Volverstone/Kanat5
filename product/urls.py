from django.urls import path
from .views import (
    CategoryListAPIView, CategoryDetailAPIView,
    ProductListAPIView, ProductDetailAPIView,
    ReviewListAPIView, ReviewDetailAPIView,
    ProductReviewsAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:id>/', ProductDetailAPIView.as_view()),
    path('products/reviews/', ProductReviewsAPIView.as_view()),

    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view()),
]

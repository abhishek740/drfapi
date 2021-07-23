from django.contrib import admin
from django.urls import path, include
from .views import *
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('addcategory/',AddCategory.as_view()),
    path('addproduct/',AddProduct.as_view()),
    path('showcatehory/',ShowCategory.as_view()),
    path('showproduct/',ShowProduct.as_view()),
    path('updatecategory/',UpdateCategory.as_view()),
    path('updateproduct/',UpdateProduct.as_view()),
    path('deletecategory/',DeleteCategory.as_view()),
    path('deleteproduct/',DeleteProduct.as_view())
  
]
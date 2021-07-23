from django import http
from django.shortcuts import render

# Create your views here.
from django.contrib.admin.sites import all_sites
from django.shortcuts import render
from rest_framework import permissions
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import status
# Create your views here.

class AddCategory(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = CategorySerializers(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

class AddProduct(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = Producterializers(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

# show all category 

class ShowCategory(APIView):
    def get(self, request):
        qs = Category.objects.all()
        ser = CategorySerializers(qs, many=True)
        return Response(ser.data)

# shaow all product 
class ShowProduct(APIView):   
    def get(self, request):
        qs = Product.objects.all()
        ser = Producterializers(qs, many=True)
        return Response(ser.data)
        

# update all category 
class UpdateCategory(APIView):
    def put(self, request):
        id = request.POST.get("id")   
        category = request.POST.get("category")        
        try:
            qs = Category.objects.get(id=id)
            if qs:
                qs.category = category
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Category Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:       
                resp = {
                    'success' : 'false',
                    'message' : "Something went wrong try again",      
                    }    
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

# UPDATE ALL PRODUCT 
class UpdateProduct(APIView):

    def put(self, request):
        id = request.POST.get("id")       
        product_name = request.POST.get("product_name")
        product_model_name = request.POST.get("product_model_name")
        price = request.POST.get("price")    
        try: 
            qs = Product.objects.get(id=id)
            if qs:
                qs.product_name = product_name
                qs.product_model_name = product_model_name
                qs.price = price
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Product Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:

            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 
            

# delete category 
class DeleteCategory(APIView):
    def delete(self, request):

        id = request.POST.get("id")  
        try:           
            qs = Category.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Category Deleted",
                    }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 

# delete product 
class DeleteProduct(APIView):
     def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Product.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Product Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 
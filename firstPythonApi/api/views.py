from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def apiOverviews(request):
  api_urls = {
    'List': 'product/'
  }
  return Response(api_urls)

# for product model
@api_view(['GET'])
def getAllProduct(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)





# def Top(request):
#   return HttpResponse("Hello Top page!")

# def Http(request):
#   return HttpResponse("Hello World!")

# def Demo(request):
#   return HttpResponse("<h1>Demo page</h1>")
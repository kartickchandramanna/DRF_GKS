from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view()
# def hellow_world(request):
#     return Response({'msg':'Hellow World'})


# @api_view(['GET'])
# def hellow_world(request):
#     return Response({'msg':'Hellow World'})


@api_view(['POST'])
def hellow_world(request):
    if request.method == "POST":
        print("POST DATA ==>", request.data)
        return Response({'msg':'This is POST request'})
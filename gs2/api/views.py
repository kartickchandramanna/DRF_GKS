from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body    # here we are collecting json data from request body
        stream = io.BytesIO(json_data)    # converting json data into stream
        python_data = JSONParser().parse(stream)  # converting into python native data type
        serializer = StudentSerializer(data = python_data)  # converting into complex data type (deserializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data saved'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = 'application/json')
            

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type = 'application/json')

    return HttpResponse("Error 404")
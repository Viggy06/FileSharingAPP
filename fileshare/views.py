from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import traceback
from .serialzers import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def download(request, uid):
    print("INSIDE DONWLOAD")
    return render(request, 'download.html', context= {"uid" : uid})

class HandleFileUpload(APIView):

    def post(self, request):
        try:
            print("INSIDE HandleFileUpload")
            data = request.data

            serializer = FileListSerializer(data = data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': "Files uploaded Successfully",
                    'data': serializer.data
                })
            
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            traceback.print_tb(e.__traceback__)
            print(e)
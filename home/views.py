from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import  APIView
from .serializers import FileListSerializer

# Create your views here.


def home(request):
    return render(request, template_name='index.html')



class HandleFileUpload(APIView):
    
    def post(self, request):
        data = request.data
        serializer = FileListSerializer(data=data)

        if  serializer.is_valid():
            serializer.save()
            return  Response({
                'status': 201,
                'files': serializer.data
            })
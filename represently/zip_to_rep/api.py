'''
from .models import Rep,Zipcode
from .serializer import RepInfoSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class ZipList(APIView):
    zips = Zipcode.objects.all()
    serialized_zips = RepInfoSerializer(zips, many=True)
    def __str__(self):
        return Response(serialized_zips.data)

class ZipDetail(APIView):
    def get_object(self):
    
'class Rep' 
'''
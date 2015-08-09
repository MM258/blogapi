from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response

from blogapi.models import *

class blogapiset(viewsets.ViewSet):
    """
    A viewset that provides the standard actions
    """
    model = About_us

    '''
    Denied Listing
    '''
    def list(self,request):
        return Response({'status':0,'error_message':'Permission Denied!!!'},
                        status=status.HTTP_400_BAD_REQUEST)
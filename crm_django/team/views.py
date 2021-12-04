import json
from rest_framework.serializers import Serializer
from datetime import datetime
import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView


from .models import Plan, Team
from .serializers import UserSerializer, PlaneSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    
    def get_queryset(self):
        """ return team members for logged in user """
        return self.queryset.filter(members__in=[self.request.user]).first()
    
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user) # m2one save
        obj.members.add(self.request.user) # m2m save 
        obj.save()
        
        
class UserDetail(APIView):
    """ user detail and update """
    def get_object(self, pk):
        """ get object """
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY
    return Response({'pub_key': pub_key})
    
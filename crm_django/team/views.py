import json
from rest_framework.serializers import Serializer
from datetime import datetime

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
        
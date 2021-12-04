from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Plan, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )
        
class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            'id',
            'name',
            'max_leads',
            'max_clients',
            'price'
        )
        
        
class TeamSerializer(serializers.ModelSerializer):
    # relational data
    members = UserSerializer(many=True, read_only=True)  # m2m
    created_by = UserSerializer(read_only=True)  # m2one
    plan = PlaneSerializer(read_only=True)  # m2one
    
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'members',
            'created_by',
            'plan',
            'plan_end_date'
        )
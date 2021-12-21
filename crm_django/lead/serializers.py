from django.db.models import fields
from rest_framework import serializers
from .models import Lead
from team.serializers import UserSerializer

class LeadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    
    class Meta:
        model = Lead
        read_only_fields = ('created_by','created', 'updated',)
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created',
            'updated'
        )
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
from stripe.api_resources import subscription

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


@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view(['POST'])
def upgrade_plan(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    plan = request.data['plan']
    print('plan', plan)
    
    if plan == 'free':
        plan = Plan.objects.get(name='Free')
    elif plan == 'smallteam':
        plan = Plan.objects.get(name='Small Team')
    elif plan == 'bigteam':
        plan = Plan.objects.get(name='Big Team')
    
    print('plan', plan)
    team.plan = plan
    team.save()
    print('team', team.plan)
    
    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view(['POST'])
def add_member(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    username = request.data['username']
    user = User.objects.get(username=username)
    team.members.add(user)
    team.save()
    return Response()  


@api_view(['POST'])
def check_session(request):
    stripe.api_key = settings.STRIPE_PUB_KEY
    error = ''

    try:
        team = Team.objects.filter(members__in=[request.user]).first()
        subscription = stripe.Subscription.retrieve(team.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)
        team.plan_status = Team.PLAN_ACTIVE
        team.plan_end_date = datetime.formtimestamp(subscription.current_period_end)
        plane = Plan.objects.get(name=product.name)
        team.plan = plane
        team.save()
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    except Exception as e:
        error = 'There something wrong. Please try again!'
        return Response({'error': error})

@api_view(['POST'])
def cancel_plan(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    plan_free = Plan.objects.get(name='Free')
    
    team.plan = plan_free
    team.plan_status = Team.PLAN_CANCELLED
    team.save()
    
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.Subscription.delete(team.stripe_subscription_id)
    except Exception as e:
        return Response({'error': 'Something went wrong. Please try again'})
    
    serializer = TeamSerializer(team)
    return Response(serializer.data)
        
        
@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    plan = data['plan']

    if plan == 'smallteam':
        price_id = settings.STRIPE_PRICE_ID_SMALL_TEAM
    else:
        price_id = settings.STRIPE_PRICE_ID_BIG_TEAM
        
    team = Team.objects.filter(members__in=[request.user]).first()
    print('--------------------------------------------------------', price_id)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [{
                'price': price_id,
                'quantity': 1
            }],
            mode = 'subscription',
            client_reference_id=team.id,
            success_url='%s?session_id={CHECKOUT_SESSION_ID}' % settings.FRONTEND_WEBSITE_SUCCESS_URL,
            cancel_url=settings.FRONTEND_WEBSITE_CANCEL_URL,
            payment_method_types = ['card'],
        )
        return Response({'sessionId': checkout_session['id']})
    except Exception as e:
        print('-----------------------------------------------------------', e)
        return Response({'error': str(e)})
    

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    print('payload', payload)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignaturVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        team = Team.objects.get(pk=session.get('client_reference_id'))
        team.stripe_customer_id = session.get('customer')
        team.stripe_subscription_id = session.get('subscription')
        team.save()

    return HttpResponse(status=200)
    
    
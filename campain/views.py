
from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework import filters
from sslcommerz_lib import SSLCOMMERZ 
from . import serializers
from . import models
import random
import string
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from account.models import UserAccount
from rest_framework.response import Response

# Create your views here.
class CampainCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Campain_Category.objects.all()
    serializer_class = serializers.CampainCategorySerializers
    lookup_field = 'slug'
    
class CampainViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CampainSerializers
    queryset = models.Campain.objects.all()
    lookup_field = 'campain_slug'
    def get_queryset(self):

        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset

class DonetionViewSet(viewsets.ModelViewSet):
    queryset = models.Donate.objects.all()
    serializer_class = serializers.DonetionSerializers
    def perform_create(self, serializer):
        donation = serializer.save()
        donar = donation.user
        campaign = donation.campaign

        print(donation.amount)
        if campaign:
            campaign.raised_price += donation.amount
            donar.total_donet_amount+=donation.amount
            print(donar)
            print(campaign)
            donar.save()
            campaign.save()


    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user')
        # print(request.user)

        if user_id :
            queryset = queryset.filter(user=user_id)

        return queryset


def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@api_view(['GET', 'POST'])
def MakePayment(request):
    donation_id = request.query_params.get('donation_id')
    print(donation_id)

    if not donation_id:
        return Response({'error': 'Donation ID is required'}, status=400)

    try:
        donation = models.Donate.objects.get(id=donation_id)
    except models.Donate.DoesNotExist:
        return Response({'error': 'Donation not found'}, status=404)

    amount = donation.amount
    print(request.user)

    settings = {
        'store_id': 'heart67ae458c8db2e',
        'store_pass': 'heart67ae458c8db2e@ssl',
        'issandbox': True
    }
    sslcz = SSLCOMMERZ(settings)

    post_body = {
        'total_amount': amount,
        'currency': "BDT",
        'tran_id': unique_transaction_id_generator(),
        'success_url': "https://heart-for-humanity-frontend.vercel.app/Profile/donationHistory.html",
        'fail_url': "your fail url",
        'cancel_url': "your cancel url",
        'emi_option': 0,
        'cus_name': donation.name,
        'cus_email': donation.email,
        'cus_phone': donation.phone,
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Donation",
        'product_category': "Charity",
        'product_profile': "general"
    }

    response = sslcz.createSession(post_body)
    print(response)

    return redirect(response['GatewayPageURL'])
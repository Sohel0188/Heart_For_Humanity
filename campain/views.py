
from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework import filters
from sslcommerz_lib import SSLCOMMERZ 
from . import serializers
from . import models
import random
import string
from rest_framework.decorators import api_view, permission_classes

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

        if user_id :
            queryset = queryset.filter(user=user_id)
        return queryset

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@api_view(['GET', 'POST'])
def MakePayment(request):

    donation_id  = request.query_params.get('donetion_id')
    # print(request)
    print(donation_id)
    # donation = models.Donate.objects.get(id=donation_id)
    # data = models.Donate.objects.all()
    # print(data)
    # payamount = donation.amount
    # print(payamount)
    # donor_name = donation.user.name 
    # donor_email = donation.user.email
    # donor_phone = donation.user.phone

    settings = { 'store_id': 'heart67ae458c8db2e', 'store_pass': 'heart67ae458c8db2e@ssl', 'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = 100
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_transaction_id_generator()
    post_body['success_url'] = "https://heart-for-humanity-frontend.vercel.app/Profile/donationHistory.html"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    response = sslcz.createSession(post_body) # API response
    print(response)

    return redirect(response['GatewayPageURL'])
    # Need to redirect user to response['GatewayPageURL']
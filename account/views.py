from django.shortcuts import render,redirect
from rest_framework import viewsets
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .import models

class UserRegistrationApiView(APIView):
    serializer_class = serializers.UserRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            author = serializer.save()
            print(author)
            token = default_token_generator.make_token(author)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(author.pk))
            print("uid ", uid)
            confirm_link = f"http://127.0.0.1:8000/account/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[author.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        
        return Response(serializer.errors)
    
def activate(request, uid64, token):
    print(uid64)
    print(token)
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        author = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        author = None 
    
    if author is not None and default_token_generator.check_token(author, token):
        author.is_active = True
        author.save()
        return redirect('http://127.0.0.1:5500/login.html')
    else:
        return redirect('http://127.0.0.1:5500/register.html')
    
# def activate(request, uid64, token):
#     try:
#         uid = urlsafe_base64_decode(uid64).decode()
#         user = User._default_manager.get(pk=uid)
#     except(User.DoesNotExist):
#         user = None 
    
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('http://127.0.0.1:5500/login.html')
#     else:
#         return redirect('http://127.0.0.1:5500/login.html')
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username)
            print(password)
            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                # userAccount = UserAccount.objects.get_or_create(user=user)
                userAccount, created = UserAccount.objects.get_or_create(author=user)
                print(userAccount)
                print(created)
                print(_) 
                login(request, user)

                return Response({'token' : token.key, 'user_id' : userAccount.id,'redirect_url': 'http://127.0.0.1:5500/'})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')


class UserprofileViewser(viewsets.ModelViewSet):
    queryset = models.UserAccount.objects.all()
    serializer_class = serializers.UserViewSerializer
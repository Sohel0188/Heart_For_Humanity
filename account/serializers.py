from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

USER_TYPE=[
    ("admin","admin"),
    ("donar","donar"),
    ]

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(required = True)
    user_type = serializers.CharField(default="donar")
    # profile_image = serializers.ImageField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password', 'confirm_password','user_type',]
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        user_type = self.validated_data['user_type']
       
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        
        models.UserAccount.objects.create(
        author = account,
        user_type = user_type,
        )
        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

# class UserViewSerializer(serializers.ModelSerializer):   
#     class Meta:
#         model = models.UserAccount
#         fields = '__all__'
# class UserViewSerializer(serializers.ModelSerializer):   

#     authorname = serializers.SerializerMethodField()

#     class Meta:
#         model = models.UserAccount
#         fields = ['username', 'phone', 'address', 'profile_image', 'user_type', 'total_donet_amount', 'author', 'authorname']
#     def get_authorname(self, obj):
#         return obj.author.username 
class UserViewSerializer(serializers.ModelSerializer):   
    username = serializers.CharField(source='author.username', read_only=True) 
    # authorname = serializers.SerializerMethodField()

    class Meta:
        model = models.UserAccount  # Correctly reference the UserAccount model
        fields = ['username', 'phone', 'address', 'profile_image', 'user_type', 'total_donet_amount', 'author']

    def get_authorname(self, obj):
        return obj.author.username
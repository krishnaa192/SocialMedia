from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User




class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['name']
        
class registerSerializer(serializers.Serializer):
    username=serializers.CharField()
    name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    def validate(self,data):
         if data['username']:
            if User.objects.filter(username=data['username']).exists():
                 raise serializers.ValidationError('username already exists')
            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError('email already exists')
            return data
    def create(self,validated_data):
        user=User.objects.create_user(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password']) 
        user.save()                            
        return validated_data

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'



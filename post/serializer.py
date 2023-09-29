from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from accounts.serializer import *


class PostSerializer(serializers.ModelSerializer):
    # Author=PersonSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
     

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'liked_by']  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['comment_to']

class SavedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPost
        fields = ['post', 'saved_user']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

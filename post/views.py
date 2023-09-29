from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework import status
from accounts.serializer import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


class PostsAPI(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        serializer=PostSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':'False','error':serializer.errors},
                             status.HTTP_400_BAD_REQUEST)
        serializer.save()   
        return Response({'status':'True','data':serializer.data},status.HTTP_201_CREATED)  
                   
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def patch(self,request):
        pk=request.data.get('id')
        post=Post.objects.get(id=pk)
        serializer=PostSerializer(post,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({'status':'False','error':serializer.errors},
                             status.HTTP_400_BAD_REQUEST)
        serializer.save()   
        return Response({'status':'True','data':serializer.data},status.HTTP_201_CREATED)
    
    def delete(self,request):
        pk=request.data.get('id')
        post=Post.objects.get(id=pk)
        post.delete()
        return Response({'status':'True','msg':'deleted'},status.HTTP_200_OK)
    
class LikeAPI(viewsets.ViewSet):
  serializer_class = LikeSerializer

  def create(self, request, id):
    liked_by_id = request.data.get('liked_by')
    post_id = id 
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response({'status': 'Error', 'message': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
       liked_by = Person.objects.get(pk=liked_by_id)
    except Person.DoesNotExist:
       return Response({'status': 'Error', 'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    post = Post.objects.get(pk=post_id)
    liked_to = post.Author
    if liked_by == liked_to:
        return Response({'status': 'Error', 'message': 'You cannot like your own post'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        like = Like.objects.get(liked_by=liked_by, liked_to=liked_to, post=post)
        like.delete()
        return Response({'status': 'unliked'})
    except Like.DoesNotExist:
        Like.objects.create(liked_by=liked_by, liked_to=liked_to, post=post)
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

class CommentAPI(viewsets.ViewSet):
    serializer_class = CommentSerializer
    
    def create(self, request, id):
        comment_by_id = request.data.get('comment_by')
        post_id = id
        comment = request.data.get('comment')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'status': 'Error', 'message': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
        try:
         comment_by = Person.objects.get(pk=comment_by_id)
        except Person.DoesNotExist:
         return Response({'status': 'Error', 'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        post = Post.objects.get(pk=post_id)
        comment_to = post.Author
        if comment_by == comment_to:
            return Response({'status': 'Error', 'message': 'You cannot comment on your own post'}, status=status.HTTP_400_BAD_REQUEST)
        Comment.objects.create(comment_by=comment_by, post=post, comment=comment, comment_to=comment_to)
        return Response({'status': 'commented'}, status=status.HTTP_201_CREATED)
    
class SavedPostAPI(viewsets.ViewSet):
    serializer_class = SavedPostSerializer
    def create(self, request, id):
        saved_user_id = request.data.get('saved_user')
        post_id = id
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'status': 'Error', 'message': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
        try:
            saved_user = Person.objects.get(pk=saved_user_id)
        except Person.DoesNotExist:
            return Response({'status': 'Error', 'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        post = Post.objects.get(pk=post_id)
        SavedPost.objects.create(saved_user=saved_user, post=post)
        return Response({'status': 'saved'}, status=status.HTTP_201_CREATED)
    
class NotificationAPI(viewsets.ViewSet):
    serializer_class = NotificationSerializer
    def create(self, request):
        user_id = request.data.get('user')
        notification = request.data.get('notification')
        try:
            user = Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return Response({'status': 'Error', 'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        Notification.objects.create(user=user, notification=notification)
        return Response({'status': 'notification sent'}, status=status.HTTP_201_CREATED)
    


class MessageAPI(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    def get(self,request):
        messages=Message.objects.all()
        serializer=MessageSerializer(messages,many=True)
        return Response(serializer.data)


    def create(self, request,id):
        user_id = id
        message = request.data.get('message')
        message_to_id = request.data.get('message_to')
        
        try:
            message_by = Person.objects.get(pk=user_id)
            
        except Person.DoesNotExist:
            return Response({'status': 'Error', 'message': 'Sender does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
        try:
            message_to = Person.objects.get(pk=message_to_id)

        except Person.DoesNotExist:
        
            return Response({'status': 'Error', 'message': 'Recipient does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        if message_by == message_to:
            return Response({'status': 'Error', 'message': 'You cannot send message to yourself'}, status=status.HTTP_400_BAD_REQUEST)
        Message.objects.create( message_by= message_by, message=message, message_to=message_to)
        return Response({'status': 'message sent'}, status=status.HTTP_201_CREATED)
    

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import LoginSerializer,registerSerializer,PersonSerializer,FollowSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication


class RegisterAPI(APIView):
    def post(self,request):
        data=request.data
        serializer=registerSerializer(data=data)
        if not serializer.is_valid():
             return Response({'status':'False','error':serializer.errors},
                              status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status':'True','data':serializer.data},status.HTTP_201_CREATED)
                                 
class LoginAPI(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':'False','error':serializer.errors},status.HTTP_400_BAD_REQUEST) 
        user=authenticate(username=data['username'],password=data['password'])
        if not user:
            return Response({'status':'False','error':'Invalid Credentials'},status.HTTP_400_BAD_REQUEST)
        token=Token.objects.get_or_create(user=user)
        return Response({'status':'True','token':str(token)},status.HTTP_200_OK)
    
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        pk=request.data.get('id')
        person=Person.objects.get(id=pk)
        serializer=PersonSerializer(person,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({'status':'False','error':serializer.errors},
                             status.HTTP_400_BAD_REQUEST)
        serializer.save()   
        return Response({'status':'True','data':serializer.data},status.HTTP_201_CREATED)
    
    def delete(self,request):
        pk=request.data.get('id')
        person=Person.objects.get(id=pk)
        person.delete()
        return Response({'status':'True','msg':'deleted'},status.HTTP_200_OK)
    
class FollowViewSet(viewsets.ViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    def post(self, request):
        data=request.data
        serializer=FollowSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':'False','error':serializer.errors},
                             status.HTTP_400_BAD_REQUEST)
        serializer.save()   
        return Response({'status':'True','data':serializer.data},status.HTTP_201_CREATED)

        
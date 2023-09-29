from django.db import models
from django.contrib.auth.models import User
import uuid

class Person(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100,unique=True)
    name=models.CharField(max_length=100)
    bio=models.TextField(blank=True,null=True)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    age=models.IntegerField(blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Follow(models.Model):
    user=models.ForeignKey(Person,on_delete=models.CASCADE)
    followed_to=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='followed_to')
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username+" has followed "+self.followed_to.username
    


from django.db import models
from django.contrib.auth.models import User
import uuid
from accounts.models import Person

# Create your models here.
class Post(models.Model):
    Author=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='author')
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images',blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)
    hashtag=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.Author.username+" has posted "+self.caption


class Message(models.Model):
    message_by=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='msguser')
    message=models.TextField()
    message_to=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='message_to')
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"{self.message_by.username} has sent a message to {self.message_to.username}"


class Like(models.Model):
    liked_by=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='user_liked')
    liked_to=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='liked_to')
    post=models.ForeignKey('Post',on_delete=models.CASCADE, related_name='post_like')
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.liked_by.username+" has liked "+self.liked_to.username +"'s post"
    
class Comment(models.Model):
    comment_by = models.ForeignKey(Person, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_to = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='comment_to')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_cmt')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return str(self.comment_by) + " has commented on " + str(self.comment_to.username) + "'s post"


class SavedPost(models.Model):
    saved_user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='saved_user')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_saved')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.saved_user.username + " has saved " + self.post.caption
    
class Notification(models.Model):
    user=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='user_notification')
    notification=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username+" has notification "+self.notification
    
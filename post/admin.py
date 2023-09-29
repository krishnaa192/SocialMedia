from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(SavedPost)
admin.site.register(Notification)


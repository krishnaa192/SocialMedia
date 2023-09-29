from . import views
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = router.urls


urlpatterns = [

    # path('', include(router.urls)),
    # path('index', views.index, name="index"),
    # path('input', views.input, name="input"),
    # path('student', views.student, name="student"),
    # # path('login', views.login, name="login"),
    path('register',RegisterAPI.as_view()),
    path('login',LoginAPI.as_view()),
    path('profile/',ProfileViewSet.as_view({'get':'list'})),
    path('profile/create',ProfileViewSet.as_view({'post':'create'})),
    path('profile/edit/<int:pk>/',ProfileViewSet.as_view({'patch':'update'})),
    path('profile/delete/<int:pk>/',ProfileViewSet.as_view({'delete':'destroy'})),
    path('follow/',FollowViewSet.as_view({'post':'post'})),
   

]
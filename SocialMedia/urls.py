
# import admin and path

from django.contrib import admin
from django.urls import path,include

# Add URL patterns to redirect the requests to the appropriate app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('', include('post.urls')),

]

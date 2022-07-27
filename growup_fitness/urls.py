from django.contrib import admin
from django.urls import path, include
from members import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers



# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('accounts/', include('authusers.urls')),

]

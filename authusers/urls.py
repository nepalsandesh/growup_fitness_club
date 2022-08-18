from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import  TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Token URL
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('logout/',LogoutAPIView.as_view(),name='logout'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    
    #accounts
    path('change-password/', ChangePasswordView.as_view(), name='changepassword'),
    path('',UsersView.as_view(), name='accounts'),
    path('<int:id>/',UserDetailsView.as_view(), name='accountsdetails'),
    path('profile/',UserProfileView.as_view(), name='userprofile'),
   ]

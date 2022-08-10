from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', api_root),
    # Token URL
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    

    #accounts
    path('change-password/', ChangePasswordView.as_view(), name='changepassword'),
    path('register/',RegisterView.as_view(), name='Register_account'),

   ]

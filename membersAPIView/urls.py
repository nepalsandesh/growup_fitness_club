from django.urls import path,include
from .views import *

urlpatterns=[
    path('', api_root),
    path('members/',MembersAPIView.as_view(),name='members'),
    path('members/<int:id>/',MemberDetails.as_view(),name='members'),
    
    path('expired-members/',ExpiredMembersAPIView.as_view(),name='expired-members'),
    # path('expired-members/<int:pk>/',ExpiredMemberDetails.as_view(),name='expired-members'),
    
    path('non-expired-members/',NonExpiredMembersAPIView.as_view(),name='non-expired-members'),
    # path('non-expired-members/<int:pk>/',NonExpiredMemberDetails.as_view(),name='non-expired-members'),
    
    path('physicalDetails/',PhysicalDetailAPIView.as_view() , name='physicalDetails'),
    path('packageDetail/',PackageDetailAPIView.as_view() , name='packageDetail'),
         
         

    
]
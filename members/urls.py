from django.urls import path, include
from .views import *

  

urlpatterns = [
    path('', MembersView.as_view(), name='members'),
    path('<int:id>/', MemberDetails.as_view(), name='member_details'),
    path('expired-members/', ExpiredMembers.as_view(), name='expired_members'),
    path('non-expired-members/', NonExpiredMembers.as_view(), name='non_expired_members'),
    path("daily-admission-data/", DailyAdmissionData.as_view(),name='daily-admission-data'),
    path("sevendays-daily-admission-data/", SevendaysDailyAdmissionData.as_view(),name='sevendays-daily-admission-data'),
    path("fourweeks-weekly-admission-data/", FourweeksWeeklyAdmissionData.as_view(),name='fourweeks-weekly-admission-data'),
    path("backup/",export,name="backup"),
   ]


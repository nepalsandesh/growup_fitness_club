from django.urls import path, include
from .views import api_root, MembersView, MemberDetails, ExpiredMembers, NonExpiredMembers

urlpatterns = [
    path('', api_root),
    # path('generics/members/',GenericsMembersView.as_view(), name='generics-members'),
    # path('generics/members/<int:pk>/',GenericsMemberDetailsView.as_view(), name='generics-memberdetails'),
    path('members/', MembersView.as_view(), name='members'),
    path('members/<int:id>/', MemberDetails.as_view(), name='member_details'),
    path('expired-members/', ExpiredMembers.as_view(), name='expired_members'),
    path('non-expired-members/', NonExpiredMembers.as_view(), name='non_expired_members'),
]


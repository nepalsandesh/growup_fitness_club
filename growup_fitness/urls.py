from django.contrib import admin
from django.urls import path, include
from members import views
from rest_framework.routers import DefaultRouter


router =  DefaultRouter()

router.register('members', views.MemberViewset, basename='members')
router.register('expired-members', views.ExpiredMemberViewset, basename='expiredmembers')
router.register('non-expired-members', views.NonExpiredMemberViewset, basename='nonexpiredmembers')
router.register('physicalDetails', views.PhysicalDetailViewset, basename='physicaldetails')
router.register('packageDetail', views.PackageDetailViewset, basename='packagedetail')

urlpatterns = [
    path('admin/', admin.site.urls),
    #Model Viewsets:
    
    # path('', include(router.urls)),
    
    # path('expired-members/', views.ExpiredMemberViewset.as_view())
    
    #APIView:
    path('', include('membersAPIView.urls'))
    
]
    
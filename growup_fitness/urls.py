from django.contrib import admin
from django.urls import path, include
from members import views
from rest_framework.routers import DefaultRouter


router =  DefaultRouter()

router.register('members', views.MemberViewset, basename='members')
router.register('expired-members', views.ExpiredMemberViewset, basename='expiredmembers')
router.register('physicalDetails', views.PhysicalDetailViewset, basename='physicaldetails')
router.register('packageDetail', views.PackageDetailViewset, basename='packagedetail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('expired-members/', views.ExpiredMembers.as_view())
    
]

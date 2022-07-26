from .models import Member, PackageDetails, PhysicalDetail
from .serializers import MemberSerializer, PackageDetailsSerializer, PhysicalDetailSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class PackageDetailViewset(viewsets.ModelViewSet):
    queryset = PackageDetails.objects.all()
    serializer_class = PackageDetailsSerializer


class PhysicalDetailViewset(viewsets.ModelViewSet):
    queryset = PhysicalDetail.objects.all()
    serializer_class = PhysicalDetailSerializer


class ExpiredMemberViewset(viewsets.ModelViewSet):
    all_packages = PackageDetails.objects.all()
    expired_packages = [x for x in all_packages if x.is_expired == True]
    expired_packages_members = [x.member for x in expired_packages]
    queryset = expired_packages_members
    serializer_class =  MemberSerializer
    

class NonExpiredMemberViewset(viewsets.ModelViewSet):
    all_packages = PackageDetails.objects.all()
    non_expired_packages = [x for x in all_packages if x.is_expired == False]
    non_expired_packages_members = [x.member for x in non_expired_packages]
    queryset = non_expired_packages_members
    serializer_class =  MemberSerializer
    


# # APIView 
# class MemberViewset(APIView):
    
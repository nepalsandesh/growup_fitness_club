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
    


# class ExpiredMembers(APIView):

#     def get(self, request, format=None):
#         all_packages = PackageDetails.objects.all()
#         expired_packages = [x for x in all_packages if x.is_expired == True]
#         expired_packages_members = [x.member for x in expired_packages]
        
#         serializer = MemberSerializer(expired_packages_members)
#         return Response(serializer.data)

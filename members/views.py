from .models import Member, PackageDetails, PhysicalDetail
from .serializers import MemberSerializer, PackageDetailsSerializer, PhysicalDetailSerializer
from rest_framework import viewsets


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
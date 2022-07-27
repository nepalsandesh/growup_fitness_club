from rest_framework.response import Response
from members.models import Member, PackageDetails, PhysicalDetail
from members.serializers import MemberSerializer, PackageDetailsSerializer, PhysicalDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import status
from django.http import HttpResponse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'members': reverse('members', request=request, format=format),
        'expired-members': reverse('expired-members', request=request, format=format),
        'non-expired-members':reverse('non-expired-members', request=request, format=format),
        'physicalDetails':reverse('physicalDetails', request=request, format=format),
        'packageDetail':reverse('packageDetail', request=request, format=format),
                
    })
    
class MembersAPIView(APIView):
    def get(self, request):
        members=Member.objects.all()
        serializer=MemberSerializer(members, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=MemberSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MemberDetails(APIView):
    def get_object(self,id):
        try:
            return Member.objects.get(id=id)
        
        except Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request,id):
        member=self.get_object(id)
        serializer=MemberSerializer(member)
        return Response(serializer.data)
    
    
    
    def put(self, request, id):
        member= self.get_object(id=id)
        serializer=MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request,id):    
        member=self.get_object(id=id)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class ExpiredMembersAPIView(APIView):
    def get(self, request):
        all_packages = PackageDetails.objects.all()
        expired_packages = [x for x in all_packages if x.is_expired == True]
        expired_members = [x.member for x in expired_packages]
        serializer=MemberSerializer(expired_members, many=True)
        return Response(serializer.data)   
    

        

    
class NonExpiredMembersAPIView(APIView):
    def get(self, request):
        all_packages = PackageDetails.objects.all()
        non_expired_packages = [x for x in all_packages if x.is_expired == False]
        non_expired_members = [x.member for x in non_expired_packages]
        serializer=MemberSerializer(non_expired_members, many=True)
        return Response(serializer.data)
    
    
    
    
class PhysicalDetailAPIView(APIView):
    def get(self, request):
        physical_detail=PhysicalDetail.objects.all()
        serializer=PhysicalDetailSerializer(physical_detail, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=PhysicalDetailSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class PackageDetailAPIView(APIView):
    def get(self, request):
        package_details=PackageDetails.objects.all()
        serializer=PackageDetailsSerializer(package_details, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=PackageDetailsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
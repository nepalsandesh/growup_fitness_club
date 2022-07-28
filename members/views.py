from django.http import HttpResponse
from .models import Member, PackageDetails
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import generics

# API Root 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        
        'members':reverse('members', request=request),
        'expired-members':reverse('expired_members', request=request),
        'non-expired-members':reverse('non_expired_members', request=request),
    })



class MembersView(APIView):

    def get(self, format=None):
        members = Member.objects.all()
        serializers = MemberSerializer(members, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        print(request.data)
        
        
        serializers = MemberSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            print("<<<<<<<<<<<<<<<<<Before Saving>>>>>>>>>>>>>>>")
            serializers.save()
            print("<<<<<<<<<<<<<<<<<<After Saving>>>>>>>>>>>>>>>>")
            return Response(serializers.data)
        print(("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>"))
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GenericsMembersView(generics.ListCreateAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer
    
    
class GenericsMemberDetailsView(generics.RetrieveUpdateAPIView):
    queryset =Member.objects.all()
    serializer_class = MemberSerializer
    

    
class MemberDetails(APIView):
    def get_object(self, id):
        try:
            return Member.objects.get(id=id)

        except Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        member = self.get_object(id)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, id):
        member= self.get_object(id=id)
        serializer=MemberSerializer(member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):    
        member=self.get_object(id=id)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ExpiredMembers(APIView):
    def get(self, request, format=None):
        all_packages = PackageDetails.objects.all()
        expired_packages = [x for x in all_packages if x.is_expired == True]
        expired_packages_members = [x.member for x in expired_packages]
        serializers = MemberSerializer(expired_packages_members, many=True)
        return Response(serializers.data)



class NonExpiredMembers(APIView):
    def get(self, request, format=None):
        all_packages = PackageDetails.objects.all()
        non_expired_packages = [x for x in all_packages if x.is_expired == False]
        non_expired_packages_members = [x.member for x in non_expired_packages]
        serializers = MemberSerializer(non_expired_packages_members, many=True)
        return Response(serializers.data)

from re import L
from rest_framework.permissions import BasePermission

from .models import Member, PackageDetails
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .dailydatagenerator import AllDailyCountData, SevendaysDailyCountData
from .weeklydatagenerator import Lastfourweeks_WeeklyCountData
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAdminUser




# API Root 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'members':reverse('members', request=request),
        'expired-members':reverse('expired_members', request=request),
        'non-expired-members':reverse('non_expired_members', request=request),
        'daily-count': reverse('daily_admission_data', request=request),
        'sevendays-daily-count': reverse('sevendays_daily_admission_data', request=request),
        'four-weeks-weekly-count': reverse('fourweeks_weekly_admission_data', request=request),

    })

    
##GENERICS CLASSES:
    
class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size=10
    

    
class MembersView(generics.ListCreateAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer
    pagination_class=BasicPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields=['member_type']
     
# Update and delete 
class MemberDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_context(self):
        print(self.request.data)

    queryset =Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field='id'
   
    
class ExpiredMembers(generics.ListAPIView):
    serializer_class=MemberSerializer
    pagination_class=BasicPagination

    def get_queryset(self):
        all_packages = PackageDetails.objects.all()
        expired_packages = [x for x in all_packages if x.is_expired == True]
        expired_packages_members = [x.member for x in expired_packages]
        expired_ids = [m.pk for m in expired_packages_members]
        expired_queryset = Member.objects.filter(pk__in=expired_ids)
        return expired_queryset

    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields=['member_type','name']
    


class NonExpiredMembers(generics.ListAPIView):
    serializer_class=MemberSerializer
    pagination_class=BasicPagination

    def get_queryset(self):
        all_packages = PackageDetails.objects.all()
        non_expired_packages = [x for x in all_packages if x.is_expired == False]
        non_expired_packages_members = [x.member for x in non_expired_packages]
        non_expired_ids = [m.pk for m in non_expired_packages_members]
        non_expired_queryset = Member.objects.filter(pk__in=non_expired_ids)
        return non_expired_queryset

    filter_backends = [filters.SearchFilter,DjangoFilterBackend]

    search_fields = ['name']
    filterset_fields=['member_type']
    
    
class DailyAdmissionData(APIView, PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    def get(self, request):     
        context=AllDailyCountData()  
        
        results = self.paginate_queryset(context, request, view=self)
        
        return self.get_paginated_response(results)
        
    
    
class SevendaysDailyAdmissionData(APIView):
    def get(self,format=None):
        context=SevendaysDailyCountData()
        return Response(context, status=status.HTTP_200_OK)


class FourweeksWeeklyAdmissionData(APIView):
    def get(self,format=None):
        context=Lastfourweeks_WeeklyCountData()
        return Response(context, status=status.HTTP_200_OK)
    

    
class DailyAdmissionDataFiltering(APIView, PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    def get(self, request, datequery):
        context=AllDailyCountData()
        selected_context=[]
        dates=datequery.split('to')
        print(dates)
        for i in context:
            if i['day']>=dates[0] and i['day']<=dates[1]:
                selected_context.append(i)
        
        results = self.paginate_queryset(selected_context, request, view=self)
        
        return self.get_paginated_response(results)
        
from rest_framework.permissions import BasePermission, IsAuthenticated
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
from datetime import date
from django.http import HttpResponse
import csv
from rest_framework.decorators import permission_classes


#Custom Pagination with inheriting PageNumberPagination
class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size=10


##GENERICS CLASSES:   
class MembersView(generics.ListCreateAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer
    pagination_class=BasicPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name','full_name','status','current_address','member_type','package_details__package_type','mobile']
    filterset_fields=['member_type','status','package_details__package_type']
     
# Update and delete 
class MemberDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset =Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field='id'
   
   
#Returns queryset of expired members 
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
    search_fields = ['name','full_name','status','current_address','member_type','package_details__package_type','mobile']    
    filterset_fields=['member_type','status']            
            
#Returns queryset of non-expired members            
class NonExpiredMembers(generics.ListAPIView):
    serializer_class=MemberSerializer
    pagination_class=BasicPagination
    def get_queryset(self):
        all_packages = PackageDetails.objects.all()
        #For todayexpiry taking keyword argument 'todayexpiry' and if its value is 1, today expiring members are returned. 
        if self.request.GET.get('todayexpiry')=='1':
            expired_packages = [x for x in all_packages if x.members_expiry_date == date.today()]
            expired_packages_members = [x.member for x in expired_packages]
            expired_ids = [m.pk for m in expired_packages_members]
            expired_queryset = Member.objects.filter(pk__in=expired_ids)
            return expired_queryset
        
        #Else if keyword argument todayexpiry is not provided then all non-expired members are returned.
        non_expired_packages = [x for x in all_packages if x.is_expired == False]
        non_expired_packages_members = [x.member for x in non_expired_packages]
        non_expired_ids = [m.pk for m in non_expired_packages_members]
        non_expired_queryset = Member.objects.filter(pk__in=non_expired_ids)
        return non_expired_queryset
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name','full_name','status','current_address','member_type','package_details__package_type','mobile']    
    filterset_fields=['member_type','status']    

    
class SevendaysDailyAdmissionData(APIView):
    def get(self,format=None):
        #Calling SevendaysDailyCountData function of dailydatagenerator.py which returns list of last seven days' guest and valid counts
        context=SevendaysDailyCountData()
        return Response(context, status=status.HTTP_200_OK)


class FourweeksWeeklyAdmissionData(APIView):
    def get(self,format=None):
        #Calling FourweekWeeklyAdmissionData function of weeklydatagenerator.py which returns list of last four weeks' guest and valid counts      
        context=Lastfourweeks_WeeklyCountData()
        return Response(context, status=status.HTTP_200_OK)
    

class DailyAdmissionData(APIView, BasicPagination):    
    def get(self, request,**kwargs): 
        #Calling AllDailyCountData function of dailydatagenerator.py which returns list of all days' guest and valid counts upto yesterday
        context=AllDailyCountData()  
        if request.GET.get("from") :
            date_lower_limit=request.GET.get("from")
            date_upper_limit=request.GET.get("to")
            selected_context=[]
            for i in context:
                if i['day']>=date_lower_limit and i['day']<=date_upper_limit:
                    selected_context.append(i)
            
            results = self.paginate_queryset(selected_context, request, view=self)
            return self.get_paginated_response(results)
        results = self.paginate_queryset(context, request, view=self)
        return self.get_paginated_response(results)
  
  
# This view function returns response of backup file and the file is downloaded automatically   

# @api_view(['GET']) 
# @permission_classes((IsAuthenticated, ))
def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Id','Member_type', 'Full_name', 'Current_address','Dob','Occupation','Mobile','Gender','Blood Group','Email','Gym Experience','Refered_by','Admission Date','Admission Charge','District','Local Gov','Ward No','Street/Tole','Country','Citizen/Passport num','Medical Problems','Emergency Contact Name','Emergency Contact Relationship','Emergency Contact Address','Emergency Contact Phone','Status','Package Type','Package Period','Convenient Time','Start Date','Package Fee','Payment Mode','Received Amount','Receipt Date','Receipt Number','Invoice Number'])
    for member in Member.objects.all().values_list('id','member_type', 'full_name', 'current_address','dob','occupation','mobile','gender','blood_group','email','gym_experience','refered_by','admission_date','admission_charge','district','local_gov','ward_no','street_or_tole','country','citizen_or_passport_num','medical_problems','emergency_contact_name','emergency_contact_relationship','emergency_contact_address','emergency_contact_phone','status','package_details__package_type','package_details__package_period','package_details__convenient_time','package_details__start_date','package_details__package_fee','package_details__payment_mode','package_details__received_amount','package_details__receipt_date','package_details__receipt_number','package_details__invoice_number'):
        writer.writerow(member)
    response['Content-Disposition'] = 'attachment; filename="gym-backup.csv"'
    return response
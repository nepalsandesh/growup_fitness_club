from .models import *
from datetime import date, timedelta


TODAY_DATE=date.today()

#This function returns list of dates from BASE_DATE to END_DATE by taking two datetime.date object parameter.
def dateslist(BASE_DATE, END_DATE):
    
    delta = END_DATE-BASE_DATE      # as timedelta
    date_list=[]
    for i in range(delta.days + 1):
        day = BASE_DATE + timedelta(days=i)
        date_list.append(day)
    return date_list

#This function returns list of all the dictionary having day belongs to last seven days:{day:"2022-08-05",guest:<guest_count>,valid:<valid_count>} 
def SevendaysDailyCountData():
    
    #BASE_DATE BEING SET to date before seven days:
    BASE_DATE=TODAY_DATE - timedelta(days=7)
    
    #For Valid member, taking admission date into consideration:
    lastseven_admission_date_data=Member.objects.filter(member_type="Valid",admission_date__gte=BASE_DATE).values("admission_date")
    lastseven_admission_date_data=[x['admission_date'] for x in lastseven_admission_date_data]
    
    #For Guest member, taking start_date into consideration:
    lastseven_start_date_data=PackageDetails.objects.filter(member__member_type="Guest",start_date__gte=BASE_DATE).values("start_date")
    lastseven_start_date_data=[x['start_date'] for x in lastseven_start_date_data]
    
    dailycount=[]
    dates_list=dateslist(BASE_DATE, TODAY_DATE)
    for i in dates_list:
        dailycount.append({'day':str(i),'guest':lastseven_start_date_data.count(i),'valid':lastseven_admission_date_data.count(i)})
        
    #Thus our desired dictionary is created as dailycount and now returning it.   
    return dailycount

#This function returns list of all the dictionary upto yesterday:{day:"2022-08-05",guest:<guest_count>,valid:<valid_count>} 
def AllDailyCountData():      
    admission_date_data=Member.objects.filter(member_type="Valid").values("admission_date")
    admission_date_data=[x['admission_date'] for x in admission_date_data]

    start_date_data=PackageDetails.objects.filter(member__member_type="Guest").values("start_date")
    start_date_data=[x['start_date'] for x in start_date_data]
    
    all_dailycount=[]
    
    #BASE_DATE MUST BE SET to some value:
    BASE_DATE=date(2022,6,1)
        
    #TAKING DATES_LIST in integer form for further operations
    dates_list=dateslist(BASE_DATE, TODAY_DATE-timedelta(days=1))
        
    for i in dates_list:
        all_dailycount.append({'day':str(i),'guest':start_date_data.count(i),'valid':admission_date_data.count(i)})       
    
    #Thus our desired dictionary is created as all_dailycount and now returning it.
    all_dailycount= all_dailycount[::-1]
    
    return all_dailycount
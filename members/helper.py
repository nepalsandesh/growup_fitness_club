from .models import *
from datetime import date, timedelta

NUMBER_OF_DAYS_IN_MONTH=[31,28,31,30,31,30,31,31,30,31,30,31]


#This function returns integer list of dates from BASE_DATE to TODAY_DATE by taking two datetime.date type parameter BASE_DATE and TODAY_DATE.
def dateslist(BASE_DATE, TODAY_DATE):
    
    delta = TODAY_DATE-BASE_DATE      # as timedelta
    date_list=[]
    for i in range(delta.days + 1):
        day = BASE_DATE + timedelta(days=i)
        date_list.append(day)
    return date_list
    
    

def AllDailyCountData():
    #For Valid member, taking admission date into consideration:
    admission_date_data=Member.objects.filter(member_type="Valid").values("admission_date")
    admission_date_data=[str(x['admission_date']) for x in admission_date_data]
    admission_date_data.sort()
    
    
    
    #For Guest member, taking start_date into consideration:
    start_date_data=PackageDetails.objects.filter(member__member_type="Guest").values("start_date")
    start_date_data=[str(x['start_date']) for x in start_date_data]
    start_date_data.sort()
      
    
    #Writing loops for returning dictionary with string date as key and their respective count as value:
    
    all_dailycount={}
    
    
    TODAY_DATE=datetime.date.today()
    
    
    #BASE_DATE MUST BE SET to some value:
    BASE_DATE=date(2022,6,1)
    
    
    
    #TAKING DATES_LIST in integer form for further operations
    dates_list=dateslist(BASE_DATE, TODAY_DATE)
    
    print("<<<<<<<<<<<<<<",dates_list)
    
    for i in dates_list:
        all_dailycount[str(i)]={'day':str(i),'guest':0,'valid':0}
    
    all_dailycount[admission_date_data[0]]['valid']=1
    
    
    for i in range(1,len(admission_date_data)):
        if admission_date_data[i]==admission_date_data[i-1]:
            all_dailycount[admission_date_data[i]]['valid']=all_dailycount[admission_date_data[i]]['valid']+1
        else:
            all_dailycount[admission_date_data[i]]['valid']=1
    
    all_dailycount[start_date_data[0]]['guest']=1
    for i in range(1,len(start_date_data)):
        if start_date_data[i]==start_date_data[i-1]:
            all_dailycount[start_date_data[i]]['guest']=all_dailycount[start_date_data[i]]['guest']+1
        else:
            all_dailycount[start_date_data[i]]['guest']=1  
            
    
    all_dailycount=[all_dailycount[x] for x in all_dailycount ]        
    #Thus our desired dictionary is created as dailycount and now returning it.
    return all_dailycount
    
    

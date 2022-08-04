from .models import *
import datetime


#This function takes python datetime datatype as argument and convert it into string. Eg:2022-08-04 to '20220804'.
def datetostr(date_data):
    year=[str(x.year) for x in date_data]
    month=[str(x.month) if len(str(x.month))==2 else str(0)+str(x.month)  for x in date_data]
    day=[str(x.day) if len(str(x.day))==2 else str(0)+str(x.day)  for x in date_data]
    str_date_data=[year[x]+month[x]+day[x] for x in range(len(year))]
    return str_date_data


def AllDailyCountData():
    #For Valid member, taking admission date into consideration:
    admission_date_data=Member.objects.filter(member_type="Valid").values("admission_date")
    admission_date_data=[x['admission_date'] for x in admission_date_data]
    str_admission_date=datetostr(admission_date_data)
    
    
    #For Guest member, taking start_date into consideration:
    start_date_data=PackageDetails.objects.filter(member__member_type="Guest").values("start_date")
    start_date_data=[x['start_date'] for x in start_date_data]
    str_start_date=datetostr(start_date_data)
    
    #Merging those two string dates and sorting:
    str_date=str_admission_date+str_start_date
    str_date.sort()
    
    
    #Writing loops for returning dictionary with string date as key and their respective count as value:

    all_dailycount={}
    
    
    today_date=[datetime.date.today()]
    today_date=datetostr(today_date)[0]
    
    for i in range(20220601,int(today_date)+1):
        all_dailycount[str(i)]=0
    
    all_dailycount[str_date[0]]=1
    
    for i in range(1,len(str_date)):
        if str_date[i]==str_date[i-1]:
            all_dailycount[str_date[i]]=all_dailycount[str_date[i]]+1
        else:
            all_dailycount[str_date[i]]=1
        
            
    #Thus our desired dictionary is created as dailycount and now returning it.
    return all_dailycount
    
    

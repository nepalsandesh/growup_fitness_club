from .models import *
from datetime import date, timedelta

TODAY_DATE=date.today()

#This function returns list of seven dates from BASE_DATE  by taking one datetime.date objecte parameter BASE_DATE.
def getsevendaysdateslist(BASE_DATE):
    
    date_list=[]
    for i in range(7):
        day = BASE_DATE + timedelta(days=i)
        date_list.append(day)
    return date_list

def Lastfourweeks_WeeklyCountData():
    
    DAYOFWEEK_TODAY=(TODAY_DATE.isoweekday() % 7)+1
    END_DATE=TODAY_DATE - timedelta(days=DAYOFWEEK_TODAY)
    BASE_DATE=END_DATE-timedelta(days=27)
    
    #For Valid member, taking admission date into consideration:
    lastfourweeks_admission_date_data=Member.objects.filter(member_type="Valid",admission_date__gte=BASE_DATE,admission_date__lte=END_DATE).values("admission_date")
    lastfourweeks_admission_date_data=[x['admission_date'] for x in lastfourweeks_admission_date_data]
    
    #For Guest member, taking start_date into consideration:
    lastfourweeks_start_date_data=PackageDetails.objects.filter(member__member_type="Guest",start_date__gte=BASE_DATE, start_date__lte=END_DATE).values("start_date")
    lastfourweeks_start_date_data=[x['start_date'] for x in lastfourweeks_start_date_data]
    
    weekly_counts=[]
    
    for i in range(0,4):
        this_week_dates=getsevendaysdateslist(BASE_DATE+timedelta(days=7*i))
        guest_count=0
        valid_count=0
        for this_week_date in this_week_dates:
            guest_count=guest_count + lastfourweeks_start_date_data.count(this_week_date)
            valid_count=valid_count+ lastfourweeks_admission_date_data.count(this_week_date)
        weekly_counts.append({'week':'week'+str(i+1),'guest':guest_count,'valid': valid_count})
                
    #weekly_counts is list of four dictionary consisting week number, guest count, valid count of last four weeks.
    return weekly_counts


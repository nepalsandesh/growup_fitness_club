from django.db import models
import datetime
from dateutil.relativedelta import relativedelta


class Member(models.Model):
    
    MEMBER_CHOICES = (
        ("Guest", "Guest Member"),
        ("Valid", "Valid Member"),
    )

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Transgender", "Transgender"),
        ("Other", "Other")
    )

    BLOOD_GROUP_CHOICES = (
        ("+AB", "AB POSITIVE"),
        ("-AB", "AB NEGATIVE"),
        ("+O", "O POSITIVE"),
        ("-O", "O NEGATIVE"),
        ("+B", "B POSITIVE"),
        ("-B", "B NEGATIVE"),
        ("+A", "A POSITIVE"),
        ("-A", "A NEGATIVE")
    )

    REFERED_BY = (
        ("Social Media", "Social Media"),
        ("Friends", "Friends"),
        ("Others", "Others")
    )
    GYM_EXPERIENCE=(
        ("Yes", "Yes"),
        ("No", "No")
    )

    member_type = models.CharField(max_length=20, choices=MEMBER_CHOICES)
    name = models.CharField(max_length=200, blank=True, null=True)
    current_address =  models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=200, null=True, blank=True )
    telephone_home = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20, blank=True, null=True)
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES, max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    gym_experience = models.CharField(max_length=150,choices=GYM_EXPERIENCE, blank=True, null=True)
    refered_by = models.CharField(choices=REFERED_BY, max_length=20, null=True, blank=True)
    admission_date = models.DateField(blank=True,null=True)
    admission_charge = models.FloatField(max_length=100, null=True, blank=True)

    full_name = models.CharField(max_length=150, blank=True)
    # permanent address
    district = models.CharField(max_length=100, blank=True)
    local_gov = models.CharField(max_length=100, blank=True)
    ward_no = models.IntegerField(blank=True, null=True)
    street_or_tole =  models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)
    citizen_or_passport_num = models.CharField(max_length=200, blank=True)
    medical_problems = models.CharField(max_length=200, blank=True)

    # Emergency contact
    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True)
    emergency_contact_address = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)

    # this is "New" or "Renew" status string, sent by frontend
    status = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.name




class PhysicalDetail(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name="physical_details",)
    weight = models.FloatField(help_text="Kgs", blank=True)
    neck = models.FloatField(help_text="inches",blank=True)
    chest = models.FloatField(help_text="inches", blank=True)
    fore_arms = models.FloatField(help_text="inches", blank=True)
    arms = models.FloatField(help_text="inches", blank=True)
    hip = models.FloatField(help_text="inches", blank=True)
    waist = models.FloatField(help_text="inches", blank=True)
    thigh = models.FloatField(help_text="inches", blank=True)
    shoulder = models.FloatField(help_text="inches", blank=True)
    calves = models.FloatField(help_text="inches", blank=True)
    height = models.FloatField(help_text="foot", blank=True)

    status = models.BooleanField(default=True)


    def __str__(self):
        return str(self.member.name)




class PackageDetails(models.Model):

    PACKAGE_TYPE = (
        ("Basic(Gym & Cardio)", "Basic(Gym & Cardio)"),
        ("Zumba(with Gym & Cardio)", "Zumba(with Gym & Cardio)"),
        ("Zumba", "Zumba")
    )

    PACKAGE_PERIOD = (
        ("Per Day", "Per Day"),
        ("Per Week", "Per Week"),
        ("Per Month", "Per Month"),
        ("1 Month", "1 Month"),
        ("3 Months", "3 Months"),
        ("6 Months", "6 Months"),
        ("1 Year", "1 Year"),
    )

    CONVENIENT_TIME = (
        ("Morning", "Morning"),
        ("Evening", "Evening"),
    )

    PAYMENT_MODE = (
        ("Cash", "Cash"),
        ("FonePay", "FonePay"),
    )

    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name="package_details")
    package_type = models.CharField(choices=PACKAGE_TYPE, max_length=50)
    package_period = models.CharField(choices=PACKAGE_PERIOD, max_length=20)
    convenient_time = models.CharField(choices=CONVENIENT_TIME, max_length=20, blank=True)
    start_date = models.DateField()
    total_fee = models.FloatField(help_text="In Rupees", blank=True)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=50, blank=True)
    received_amount = models.FloatField(help_text="In Rupees", default=0, null=True, blank=True)
    receipt_date = models.DateField(blank=True, null=True)
    receipt_number = models.CharField(max_length=50, blank=True, null=True)
    invoice_number = models.CharField(max_length=50, blank=True, null= True)

    status = models.BooleanField(default=True)
    



    def __str__(self):
        return "{}-{}-{}months".format( self.member, self.package_type, self.package_period)

    @property
    def members_expiry_date(self):
        start_date = self.start_date
        expiry_Date = start_date

        if self.package_period == "Per Day":
            expiry_Date = start_date + relativedelta(days=1)

        elif self.package_period == "Per Week":
            expiry_Date = start_date + relativedelta(weeks=1)

        elif self.package_period == "Per Month":
            expiry_Date = start_date + relativedelta(months=1)

        elif self.package_period == "1 Month":
            expiry_Date = start_date + relativedelta(months=1)
        
        elif self.package_period == "3 Months":
            expiry_Date = start_date + relativedelta(months=3)

        elif self.package_period == "6 Months":
            expiry_Date = start_date + relativedelta(months=6)

        elif self.package_period == "1 Year":
            expiry_Date = start_date + relativedelta(months=12)

        return expiry_Date

    @property
    def is_expired(self):
        if self.members_expiry_date < datetime.date.today():
            return True
        else:
            return False 

    @property 
    def due_amount(self):
        amount = self.total_fee - self.received_amount
        return float(amount)



        

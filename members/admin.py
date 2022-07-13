from django.contrib import admin
from .models import Member, PackageDetails, PhysicalDetail

# Register your models here.
admin.site.register(Member)
admin.site.register(PackageDetails)
admin.site.register(PhysicalDetail)

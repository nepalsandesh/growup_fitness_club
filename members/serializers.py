from rest_framework import serializers
from .models import Member, PackageDetails, PhysicalDetail



class PackageDetailsSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()
    members_expiry_date = serializers.SerializerMethodField()


    class Meta:
        model = PackageDetails  
        exclude = ['id', 'member']
        extra_fields = ['is_expired', 'members_expiry_date']

    def get_is_expired(self, instance):
        return instance.is_expired


    def get_members_expiry_date(self, instance):
        return instance.members_expiry_date



class PhysicalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalDetail
        exclude = ['id', 'member']



class MemberSerializer(serializers.ModelSerializer):
    physical_details = PhysicalDetailSerializer()
    package_details = PackageDetailsSerializer()


    class Meta:
        model = Member
        fields = '__all__'
        extra_fields = ['physical_details', 'package_details']

    def create(self, validated_data):
        physical_detail_data = validated_data.pop("physical_details")   
        package_detail_data = validated_data.pop("package_details")

        member = Member.objects.create(**validated_data)
        PhysicalDetail.objects.create(member=member, **physical_detail_data)
        PackageDetails.objects.create(member=member, **package_detail_data)
        return member
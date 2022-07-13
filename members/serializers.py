from rest_framework import serializers
from .models import Member, PackageDetails, PhysicalDetail



class PackageDetailsSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()
    members_expiry_date = serializers.SerializerMethodField()

    
    class Meta:
        model = PackageDetails  
        exclude = ['id']
        extra_fields = ['is_expired', 'members_expiry_date']

    def get_is_expired(self, instance):
        return instance.is_expired


    def get_members_expiry_date(self, instance):
        return instance.members_expiry_date



class PhysicalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalDetail
        exclude = ['id']



class MemberSerializer(serializers.ModelSerializer):
    physical_details = PhysicalDetailSerializer(many=True)
    package_details = PackageDetailsSerializer(many=True)


    class Meta:
        model = Member
        fields = '__all__'
        extra_fields = ['physical_details', 'package_details']

    def create(self, validated_data):
        print("create hit")
        physical_detail_data = validated_data.pop("physical_details")
        package_detail_data = validated_data.pop("package_details")


        member = Member.objects.create(**validated_data)
        PhysicalDetail.objects.create(member=member, **physical_detail_data)
        PackageDetails.objects.create(member=member, **package_detail_data)
        return member















# class AllDataSerializer(serializers.Serializer):
#     member = MemberSerializer(many=True)
#     package = PackageDetailsSerializer(many=True)
#     physical = PhysicalDetailSerializer(many=True)



#     def data_return():
#         return fields

# member_serialize_data = MemberSerializer()
# package_detail_serializers = PackageDetailsSerializer()
# physical_detail = PhysicalDetailSerializer()

# class CustomSerializedData():
#     member_serialize_data = member_serialize_data.fields
#     package_detail_serializers = package_detail_serializers.fields
#     physical_detail = physical_detail.fields

#     data = [member_serialize_data, package_detail_serializers, physical_detail]
#     for i in data:
#         def return_dict_type(i):
#             data = dict(i.fields)
#             return data
            



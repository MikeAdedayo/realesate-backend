from rest_framework import serializers

from .models import Tenant,TenantProfile,HouseRent,Waste,Complain

class TenantSerializer(serializers.ModelSerializer):

     class Meta:
             model = Tenant
             fields = '__all__'

# class PayHouseRentSerializer(serializers.0)
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TenantProfile
        fields = '__all__'

class HouseRentSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseRent
        fields = '__all__'

class WasteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waste
        fields = '__all__'

class ComplainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complain
        fields = '__all__'

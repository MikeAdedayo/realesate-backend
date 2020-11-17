from django.contrib import admin

from .models import Tenant,TenantProfile,Apartment,HouseRent,Waste,Complain
admin.site.register(Apartment)
admin.site.register(TenantProfile)
admin.site.register(Tenant)
admin.site.register(HouseRent)
admin.site.register(Waste)
admin.site.register(Complain)
from django.db import models

class Apartment(models.Model):
    building_title = models.CharField(max_length=50)
    flat_title = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    toilet = models.IntegerField()
    tenacy_rate = models.IntegerField()

    def __str__(self):
        return self.flat_title

class Tenant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    moved_in = models.DateTimeField(auto_now_add=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    caution_fee = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class TenantProfile(models.Model):
    profile = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=50)
    gender = models.CharField(max_length=7)
    marital_status = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    State_of_origin = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50)
    Spouse_name = models.CharField(max_length=50)
    telphone_no = models.CharField(max_length=50)
    office_addr = models.CharField(max_length=500)
    previous_home_addr = models.CharField(max_length=500)
    sponsor_addr = models.CharField(max_length=500)
    sponsor_phone = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.profile.username


class HouseRent(models.Model):
    rent_by = models.ForeignKey(Tenant,  on_delete=models.CASCADE)
    year_for = models.IntegerField()
    date = models.DateTimeField()
    amount = models.IntegerField()

    def __str__(self):
        return 'rent by ' + self.rent_by.username + 'for ' + self.year_for

class Waste(models.Model):
    waste_by = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    month_for = models.CharField(max_length=20)
    date = models.DateTimeField()
    amount = models.IntegerField()

    def __str__(self):
        return 'waste by ' + self.waste_by.username + 'for ' + self.month_for

class Complain(models.Model):
    complain_by = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)
    status = models.BooleanField(default=False)














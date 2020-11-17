from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from paystackapi.paystack import Paystack
from django.http import HttpResponse
from django.core import serializers

from .models import Tenant,TenantProfile,HouseRent,Apartment,Waste,Complain
from .serializers import TenantSerializer,ProfileSerializer,HouseRentSerializer,WasteSerializer,ComplainSerializer
import json

class TenantList(APIView):

    def get(self, request):
        tenants = Tenant.objects.all()
        serializer = TenantSerializer(tenants,many=True)
        return Response(serializer.data)

class PayHouseRent(APIView):
    def get(self, request):
        paystack_secret_key = "sk_test_9e2450a9dfb7daf8e8f4cc34c2aea150dc54536d"
        paystack = Paystack(secret_key=paystack_secret_key)
        from paystackapi.transaction import Transaction
        response = paystack.transaction.initialize(reference='2019chhouserentmk',
                                          amount=10000, email='topemichealodediran@gmail.com')
        return(response)
        # return Response(response)

class Login(APIView):
        # return data
    def post(self,request):
        reponse = ""
        data = request.data
        try:
            user = Tenant.objects.get(username=data['username'])
            if user.password == data['password']:

                reponse = "sucessful"
            else:
                reponse = "invalid password"

        except Tenant.DoesNotExist:
                reponse = "invalid username"
        except:
             reponse = "invalid"


        mk = '{"response":"' + reponse + '"}'
        loginResponse = json.loads(mk)
        return Response(loginResponse)

class Profile(APIView):
    def get(self,request,username):
        user = Tenant.objects.get(username=username)
        profile = user.tenantprofile_set.all()
        profile.firstName = user.first_name
        profile.lastName = user.last_name
        serializer = ProfileSerializer(profile, many=True)

        return Response(serializer.data)

class HouseRent(APIView):
    def get(self,request,username):
        houseRent = Tenant.objects.get(username=username).houserent_set.all()
        serializer = HouseRentSerializer(houseRent, many=True)
        return Response(serializer.data)

class Wastefee(APIView):
    def get(self,request,username):
        waste = Tenant.objects.get(username=username).waste_set.all()
        serializer = WasteSerializer(waste, many=True)
        return Response(serializer.data)

class ComplainData(APIView):
    def get(self,request,username):
        username = str(username)
        complain = Tenant.objects.get(username=username).complain_set.all()
        serializer = ComplainSerializer(complain, many=True)
        return Response(serializer.data)

    def post(self,request,username):
        data = request.data
        subject = data['subject']
        message = data['message']
        complian = Tenant.objects.get(username=username).complain_set.create(subject=subject,message=message)
        complian.save()
        reponse= 'sucess'
        mk = '{"response":"' + reponse + '"}'
        ComplainResponse = json.loads(mk)
        return Response(ComplainResponse)

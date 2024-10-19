from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics,status
from rest_framework.response import Response 
from rest_framework.views import APIView

from .models import *
from .serializers import *

class BanksAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class =  BankSerializer
class BanksDetailsAPIView(generics.RetrieveDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class =  BankSerializer

    
# END BANKS


# START BRANCHES
    
    
class BranchesAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class =  BranchSerializer
    
class BranchesDetailsAPIView(generics.RetrieveDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class =  BranchSerializer
    
    
# END BRANCHES

# START ACCOUNTS

class CreateAccountAPIView(APIView):
    def post(self,request):
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import userSerializer
from .models import  User


class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = userSerializer
    
    
from rest_framework import viewsets

from .serializers import employeeSerializer
from .models import Employee


class employeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('first_name')
    serializer_class = employeeSerializer

    
    
    
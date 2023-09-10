from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Company,Employee
from myapp.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyViewsSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            Company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(Company=Company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':0
            })
        
    
    
    
class EmployeeViewsSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
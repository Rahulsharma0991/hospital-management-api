from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import Patient_serializers,Doctor_serializers,Appointment_serializers
from .models import Patient,Doctor,Appointment
from rest_framework.permissions import BasePermission
from .permission import mypermission
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# REGISTER 
class Register(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"Message":'Username already taken...'})
        user=User.objects.create_user(username=username,password=password)
        return Response({"Message":"User created sucessfully...."})
    
# LOGIN

class Login(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)

        if user:
            refresh=RefreshToken.for_user(user)
            return Response({
                'refersh':str(refresh),
                "access":str(refresh.access_token)
            })
        return Response({"Error":"credential error...."})
    
class Check(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
         return Response({

            "message":"Welcome",

            "user":request.user.username
        })
    
# Patient_CRUD

class Patient_viewset(ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=Patient_serializers

# DoctorSerializer
class Doctor_viewset(ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=Doctor_serializers

# filter
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filter_fields=['specialization',"name"]
    search_fields='name'
# AppointmentSerializer
class Appointment_viewset(ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class = Appointment_serializers
   




from rest_framework import viewsets
from rest_framework import generics
from rest_framework .response import  Response 
#Create your views here.
from .models import Login
from .serializers import LoginSerializer
class LoginViewSets(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer






  


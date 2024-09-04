from django.shortcuts import render
from Leadmodules.models import Leadmodules
from .forms import Leadmoduleform
from django.http import HttpResponse
from rest_framework import permissions
from .serializers import Leadserializer
from rest_framework import viewsets
from . import forms

# Create your views here.


class CreateNewLeadViewSet(viewsets.ModelViewSet):

    queryset = Leadmodules.objects.all()
    serializer_class = Leadserializer
    permission_classes=[permissions.IsAuthenticated]

def  addmodule(request):

        f=forms.Leadmoduleform()
        if Leadmodules.method=="POST":
            f=Leadmoduleform(request.POST)
            if f.is_valid():
                f.save()
                print(f.is_valid())
                return HttpResponse("Data submitted")
            else:
                print(f.is_valid)
                print(f.errors)
        else:
            f= Leadmoduleform()

                    







from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import CreateLeads
from .serializers import CreateLeadsSerializer
# Create your views here.

class CreateLeadsViewSet(viewsets.ModelViewSet):

    queryset = CreateLeads.objects.all()
    serializer_class = CreateLeadsSerializer

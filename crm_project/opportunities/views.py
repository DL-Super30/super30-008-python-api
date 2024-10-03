from django.shortcuts import render
from rest_framework import viewsets
from .models import opportunities
# from rest_framework import permissions


from .serializers import opportunitiesSerializer
# Create your views here.

class opportunitiesViewSet(viewsets.ModelViewSet):

    queryset =opportunities.objects.all()
    serializer_class = opportunitiesSerializer
    # permission_classes=[permissions.IsAuthenticated]

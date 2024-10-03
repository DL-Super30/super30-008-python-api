from django.shortcuts import render
from rest_framework import viewsets
from .models import learners
from rest_framework import permissions

# Create your views here.
from.serializers import  LearnersSerializers
class learnersViewSet(viewsets.ModelViewSet):
        queryset =learners.objects.all()
        serializer_class = LearnersSerializers
        permission_classes=[permissions.IsAuthenticated]

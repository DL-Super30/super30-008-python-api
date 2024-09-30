from django.shortcuts import render
from rest_framework import viewsets
from .models import  Courses

# Create your views here.

from .serializers import CoursesSerializers


class  CoursesViewSet(viewsets.ModelViewSet):
        queryset = Courses.objects.all()
        serializer_class =  CoursesSerializers



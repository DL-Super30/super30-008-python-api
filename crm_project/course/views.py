from django.shortcuts import render
from rest_framework import viewsets
from .models import  Courses
# from rest_framework import permissions

# Create your views here.

from .serializers import CoursesSerializers


class  CoursesViewSet(viewsets.ModelViewSet):
        queryset = Courses.objects.all()
        serializer_class =  CoursesSerializers
        # permission_classes=[permissions.IsAuthenticated]



from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
import pytz
from .models import CreateLeads
from .serializers import CreateLeadsSerializer
# Create your views here.

class CreateLeadsViewSet(viewsets.ModelViewSet):

    queryset = CreateLeads.objects.all()
    serializer_class = CreateLeadsSerializer



# def Leads(request):
    
#         local_timezone = pytz.timezone('Asia/Kolkata') 
#         for item in Leads:
#           if item.date_field:  # Ensure date_field is not None
#             item.local_time = item.date_field.astimezone(local_timezone)

#         return render(request,  {'items': Leads})
      



   

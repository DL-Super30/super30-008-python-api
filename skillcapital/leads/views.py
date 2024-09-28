from rest_framework import viewsets
from .models import leads   
from django.shortcuts import render
from .serializers import Leadserializers
import pytz
# Create your views here.


class LeadViewSet(viewsets.ModelViewSet):

    queryset=leads.objects.all()
    serializer_class=Leadserializers

    
    def leads(request):

        local_timezone = pytz.timezone('Asia/Kolkata') 
        for item in leads:
          if item.date_field:  # Ensure date_field is not None
            item.local_time = item.date_field.astimezone(local_timezone)

        return render(request, 'item_list.html', {'items': leads})
      
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for event in response.data:
            event['Datetime'] = event['Datetime'].replace(tzinfo=None)  # Remove timezone info
        return response

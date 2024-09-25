from rest_framework import viewsets
from .models import leads   
from .serializers import Leadserializers
# Create your views here.
class LeadViewSet(viewsets.ModelViewSet):

    queryset=leads.objects.all()
    serializer_class=Leadserializers
    

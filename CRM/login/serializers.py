from rest_framework import serializers 
from .models import Loginuser

class Leadserializer(serializers.ModelSerializer):

    class Meta:

        model=Loginuser
        fields ="__all__"
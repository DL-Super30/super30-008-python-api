from rest_framework import serializers 
from .models import Leadmodule

class Leadserializer(serializers.ModelSerializer):

    class Meta:

        model=Leadmodule
        fields ="__all__"
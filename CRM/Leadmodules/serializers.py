from rest_framework import serializers 
from .models import Leadmodule

class Leadserializer(serializers.Modelserializer):

    model=Leadmodule
    fields ="__all__"
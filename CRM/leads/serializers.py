from rest_framework import serializers
from .models import leads

class Leadserializers(serializers.ModelSerializer):

    class Meta :

        model= leads
        fields="__all__"
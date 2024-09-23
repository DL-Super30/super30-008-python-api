from rest_framework import serializers
from .models import opportunities

class opportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = opportunities
        fields = '__all__'
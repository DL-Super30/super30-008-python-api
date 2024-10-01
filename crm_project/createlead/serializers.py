from rest_framework import serializers
from .models import CreateLeads
# from django.utils import timezone


class CreateLeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateLeads
        fields = '__all__'

        
# def get_start_time(self, obj):
#     naive_time = timezone.make_naive(obj.start_time)
#     return naive_time.strftime('%Y-%m-%d %H:%M:%S')


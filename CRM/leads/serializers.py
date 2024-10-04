from rest_framework import serializers
from .models import leads
from django.utils import timezone

class Leadserializers(serializers.ModelSerializer):

    class Meta :

        model= leads
        fields="__all__"

    def get_start_time(self, obj):
        naive_time = timezone.make_naive(obj.start_time)
        return naive_time.strftime('%Y-%m-%d %H:%M:%S')
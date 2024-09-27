from rest_framework import serializers
from.models import learners


class LearnersSerializers(serializers.ModelSerializer):

    class Meta:
       model = learners
       fields ='__all__'

from rest_framework import serializers
from analytics.models import Pupil

class PupilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pupil
        fields = '__all__'

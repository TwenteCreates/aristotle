from rest_framework import serializers
from analytics.models import Pupil, Concept, ConceptRelation


class ConceptRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptRelation
        fields = ['from_concept', 'to_concept', 'level']


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = '__all__'


class ConceptSerializer(serializers.ModelSerializer):

    related = ConceptRelationSerializer(source='get_related_concepts',many=True)

    class Meta:
        model = Concept
        fields = '__all__'

from rest_framework import generics, viewsets
from analytics.serializers import *
from analytics.models import *


class PupilView(viewsets.ViewSetMixin, generics.ListAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    filter_fields = [getattr(field, 'name') for field in Pupil._meta.fields]


class ConceptView(viewsets.ViewSetMixin, generics.ListAPIView):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    filter_fields = [getattr(field, 'name') for field in Concept._meta.fields]


class PrimarySchoolView(viewsets.ViewSetMixin, generics.ListAPIView):
    queryset = PrimarySchool.objects.all()
    serializer_class = PrimarySchoolSerializer
    filter_fields = [getattr(field, 'name') for field in PrimarySchool._meta.fields]

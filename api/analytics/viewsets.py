from rest_framework import viewsets
from analytics.serializers import PupilSerializer
from analytics.models import Pupil

class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer

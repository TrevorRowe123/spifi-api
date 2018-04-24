from spifiapi.models import Sensor, Target
from rest_framework import viewsets
from spifiapi.serializers import SensorSerializer, TargetSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
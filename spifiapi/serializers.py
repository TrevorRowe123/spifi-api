import models
from rest_framework import serializers


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('lat', 'lng')


class TargetSerializer(serializers.HyperlinkedModelSerializer):
    targetLng = serializers.Field(source='getTargetLat')
    targetLat = serializers.Field(source='getTargetLng')
    class Meta:
        model = Target
	read_only_fields = ('targetLat', 'targetLng')
        fields = ('sensor', 'time', 'addr')
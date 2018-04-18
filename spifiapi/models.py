from django.db import models

# Create your models here.

class Sensor(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.id

class Target(models.Model):
    time = models.DateTimeField
    sensor = models.ManyToManyField(Sensor)
    addr = models.CharField(max_length = 20)
	
    def getTargetLat(self):
        return sensor.lat

    def getTargetLng(self):
        return sensor.lng

    def __str__(self):
        return self.addr
	

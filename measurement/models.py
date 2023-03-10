from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256, default='')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default=None, null=True)
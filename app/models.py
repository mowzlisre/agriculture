from django.db import models

class Record(models.Model):
    moist_1 = models.IntegerField(default=0)
    moist_2 = models.IntegerField(default=0)
    temp = models.IntegerField(default=0)
    rain = models.IntegerField(default=0)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.timestamp)
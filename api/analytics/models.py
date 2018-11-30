from django.db import models

class Pupil(models.Model):
    gender = models.BooleanField();
    recommendation = models.CharField(max_length=30)

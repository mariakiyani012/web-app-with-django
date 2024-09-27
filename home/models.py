from django.db import models

# Create your models here.
class Schedule(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    contact = models.CharField(max_length=12)
    date = models.DateTimeField()
    desc = models.CharField(max_length=122)

    def __str__(self):
        return self.name
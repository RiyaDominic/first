from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    def __str__(self):
        return self.name
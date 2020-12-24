from django.db import models

class Types(models.Model):
    in_arabic = models.CharField(max_length=20)
    in_latine  = models.CharField(max_length=20)
    in_tifinigh= models.CharField(max_length=20)

    def __str__(self):
        return self.in_arabic+"/"+self.in_latine+"/"+self.in_tifinigh

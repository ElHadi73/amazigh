from django.db import models
from .types import Types
from tinymce.models import HTMLField

class Word(models.Model):
    in_arabic   = models.CharField(max_length=20)
    in_latine   = models.CharField(max_length=20)
    in_tifinigh = models.CharField(max_length=20)
    Definition  = HTMLField()
    many_means  = models.ManyToManyField("self",blank=True)
    opst_words  = models.ManyToManyField("self",blank=True)
    racine_id   = models.ForeignKey('Word',on_delete=models.PROTECT,null=True,blank=True)
    type_id     = models.ForeignKey(Types,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return self.in_arabic+"/"+self.in_latine+"/"+self.in_tifinigh

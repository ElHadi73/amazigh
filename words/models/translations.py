from django.db import models
from .wordamazigh import Word
from .languages import Languages

class translations(models.Model):
    lang_id     = models.ForeignKey('Languages',on_delete=models.PROTECT,)
    ama_words   = models.ManyToManyField(Word)
    traduction  = models.CharField(max_length=20,blank=False,null=False)
    Description = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.traduction


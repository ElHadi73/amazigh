from django.db import models
from .types import Types
from .languages import Languages

class Types_translations(models.Model):
    type_id = models.ForeignKey(Types,on_delete=models.CASCADE)
    lang_id = models.ForeignKey(Languages,on_delete=models.CASCADE)
    translation = models.CharField(max_length=20,primary_key=True)


from django.db import models

class Languages(models.Model):
    language = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.language.title()

    def in_langs():
        langs=[]
        for i in Languages.objects.all():
            langs.append([i.language,i.id])
        return langs[:]

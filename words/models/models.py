from django.db import models
from words.models.wordamazigh import Word
from words.models.translations import translations

#Create your models here.
def detect_ama(ama):
    detect=[]
    asci=["False","False","False"]
    for i in ama:
        detect.append(ord(i))
    for i in detect:
        if i <= 11647 and i>=11568:                         #amazigh keywords
            asci[0]="True"
        elif(i<=90 and i >=65) or (i<=122 and i>=97):       #latine keywords
            asci[1]="True"
        elif i<=1791 and i>=1536:                           #arabic keywords
            asci[2]="True"
        else:
            asci[0]="False"
            asci[1]="False"
            asci[2]="False"
        #asci=[amazigh, latine, arabic]
    c=0
    for i in asci:
        if i=="True":
            c=c+1
    if c==1:
        if asci[0]=="True":
            return 0
        elif asci[1]=="True":
            return 1
        elif asci[2]=="True":
            return 2
    else:
        return "False"
def search_result(inlang,outlang,userinput):
    if inlang=="Amazigh" and outlang=="Amazigh":
        l=detect_ama(userinput)
        if l=="False":
            return "False"
        elif l==0:
            obj=Word.objects.get(in_tifinigh=userinput)
        elif l==1:
            obj=Word.objects.get(in_latine=userinput)
        elif l==2:
            obj=Word.objects.get(in_arabic=userinput)
            
        typ=obj.type_id
        many_list=[[i.in_arabic,i.in_latine,i.in_tifinigh] for i in obj.many_means.all()]
        oppo_list=[[i.in_arabic,i.in_latine,i.in_tifinigh] for i in obj.opst_words.all()]
        racine=[obj.racine_id.in_tifinigh,obj.racine_id.in_latine,obj.racine_id.in_arabic]
        return [[obj.in_arabic,typ.in_arabic]    ,
                [obj.in_latine,typ.in_latine]    ,
                [obj.in_tifinigh,typ.in_tifinigh],1,many_list[:],oppo_list[:],obj.Definition,racine]
    elif inlang=="Amazigh":
        l=detect_ama(userinput)
        if l=="False":
            return "False"
        elif l==0:
            obj=Word.objects.get(in_tifinigh=userinput)
        elif l==1:
            obj=Word.objects.get(in_latine=userinput)
        elif l==2:
            obj=Word.objects.get(in_arabic=userinput)
        typ=obj.type_id.types_translations_set.get(lang_id=outlang).translation
        many_list=[[i.traduction,i.Description] for i in obj.translations_set.all().filter(lang_id=outlang)]
        return [many_list,None,typ,2]
    elif outlang=="Amazigh":
        obj=translations.objects.get(lang_id=inlang,traduction=userinput).ama_words.first()
        typ=obj.type_id
        many_list=[[i.in_arabic,i.in_latine,i.in_tifinigh] for i in obj.many_means.all()]
        return [many_list[:]]
from django.shortcuts import render
from words.models.languages import Languages
from words.models import models
from words.models.wordamazigh import Word

# Create your views here.
def home(request,word=None,input_lang=None,*args,**kwargs):
    output=[]
    context={}
    tit=""
    if 'search_text' in request.GET:
        get=request.GET
        tit=get['search_text']
        output=models.search_result(get['input_lang'],get['output_lang'],get['search_text'])
    elif word!=None and input_lang==None:
        tit=word
        output=models.search_result("Amazigh","Amazigh",word)
    context={"langs":Languages.in_langs(),'output':output,"tit":tit}
    return render(request,"home.html",context)
def home2(request,word=None,input_lang=None,*args,**kwargs):
    output=[]
    context={}
    tit=""
    tit=word
    output=models.search_result(input_lang,"Amazigh",word)
    context={"langs":Languages.in_langs(),'output':output,"tit":tit}
    return render(request,"home.html",context)


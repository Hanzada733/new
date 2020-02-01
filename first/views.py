from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from googletrans import Translator
translator = Translator()
"""en 
ru 
kk
"""
from .forms import *
# Create your views here.
class IndexView(View):
    def get(self,request):
        form=Prosto_form
        return render(request,'index.html',locals())
    def post(self,request):
        text = request.POST.get('name')
        result = translator.translate(text=text, src='ru', dest='en')
        res = result.text
        return HttpResponse(res)

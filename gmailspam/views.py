# coding=utf-8
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from pyvi.pyvi import ViTokenizer
from .models import Extracted
from langdetect import detect
import requests


class TokenizeView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        for m in Extracted.objects.filter(tokenize__isnull=True):
            print(m.id, m.lang)
            if m.lang == "vi":
                m.tokenize = ViTokenizer.tokenize(m.normalized)
            else:
                m.tokenize = m.normalized
            m.save()
        return super(TokenizeView, self).render_to_response(context, **response_kwargs)


class LangDetectView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        Extracted.objects.filter(normalized__isnull=True).delete()
        for m in Extracted.objects.filter(lang__isnull=True):
            try:
                m.lang = detect(m.normalized)
                print(m.id, m.lang)
                m.save()
            except:
                m.lang = "error"
                m.save()
                print(m.id, "error")
        Extracted.objects.exclude(lang__in=["vi", "en"]).delete()
        return super(LangDetectView, self).render_to_response(context, **response_kwargs)
# homepage
class HomePageView(TemplateView):
    template_name = "index.html"

#fucntion return result from server
def returnResult(request):
    inputEmail = request.POST.get("inputEmail","")
    print(inputEmail)
    tokenize = ViTokenizer.tokenize(inputEmail)
    lang = detect(inputEmail)

    if lang != 'vi':
        lang = "en"

    data = {
        'lang':lang,
        'text':tokenize
    }

    response = requests.post("http://localhost:5000/predict",json=data)
    return HttpResponse(response)

# coding=utf-8
from django.views.generic import TemplateView
from pyvi.pyvi import ViTokenizer, ViPosTagger
from models import Extracted
from langdetect import detect


class TokenizeView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        for m in Extracted.objects.filter(tokenize__isnull=True, lang="vi"):
            print m.id
            m.tokenize = ViTokenizer.tokenize(m.normalized)
            m.save()
        return super(TokenizeView, self).render_to_response(context, **response_kwargs)


class LangDetectView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        Extracted.objects.filter(normalized__isnull=True).delete()
        for m in Extracted.objects.filter(lang__isnull=True):
            try:
                m.lang = detect(m.normalized)
                print m.id, m.lang
                m.save()
            except:
                m.lang = "error"
                m.save()
                print m.id, "error"
        Extracted.objects.exclude(lang__in=["vi", "en"]).delete()
        return super(LangDetectView, self).render_to_response(context, **response_kwargs)
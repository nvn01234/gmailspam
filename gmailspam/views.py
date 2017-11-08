# coding=utf-8
import random

from django.views.generic import TemplateView
from pyvi.pyvi import ViTokenizer
from models import Extracted
from langdetect import detect


class TokenizeView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        for m in Extracted.objects.filter(tokenize__isnull=True):
            print m.id, m.lang
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
                print m.id, m.lang
                m.save()
            except:
                m.lang = "error"
                m.save()
                print m.id, "error"
        Extracted.objects.exclude(lang__in=["vi", "en"]).delete()
        return super(LangDetectView, self).render_to_response(context, **response_kwargs)


class ShuffleTrainTestView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        ids = [x.id for x in Extracted.objects.all()]
        random.shuffle(ids)
        pos = int(len(ids)*0.3)
        data_test = ids[:pos]
        data_train = ids[pos:]
        Extracted.objects.filter(id__in=data_test).update(data_set="test")
        Extracted.objects.filter(id__in=data_train).update(data_set="train")
        return super(ShuffleTrainTestView, self).render_to_response(context, **response_kwargs)
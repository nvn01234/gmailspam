from django.db import models


class Extracted(models.Model):
    raw = models.TextField()
    normalized = models.TextField()
    tokenize = models.TextField()
    lang = models.CharField(max_length=255, null=True)
    label = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'extracted'
        app_label = 'extracted'

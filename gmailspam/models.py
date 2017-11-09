from django.db import models


class Extracted(models.Model):
    id = models.IntegerField()
    raw = models.TextField()
    normalized = models.TextField()
    tokenize = models.TextField()
    lang = models.CharField(max_length=255, null=True)
    label = models.CharField(max_length=255, null=True)
    numOfImage = models.IntegerField(null=True)
    numOfLink = models.IntegerField(null=True)

    class Meta:
        db_table = 'extracted'
        app_label = 'extracted'

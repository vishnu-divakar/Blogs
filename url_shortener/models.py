from django.db import models

class UrlModel(models.Model):
    id = models.CharField(primary_key = True, max_length = 255)
    url = models.CharField(max_length = 255)

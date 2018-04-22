from django.db import models

class BlogPostModel(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    username = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now= True)



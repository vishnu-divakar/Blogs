from django.db import models
from blog_post.models import BlogPostModel

class CommentManager(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 25, blank=True, null=True)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(BlogPostModel, on_delete = models.CASCADE)
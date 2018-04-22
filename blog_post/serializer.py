from blog_post.models import BlogPostModel
from rest_framework import serializers

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = ("id", "title", "content", "username", "created_time", "updated_time")
        
from rest_framework import serializers
from comment_manager.models import CommentManager

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentManager
        fields = ("id", "name", "comment", "created_time", "updated_time","post")
        
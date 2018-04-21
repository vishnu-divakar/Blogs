from rest_framework import serializers
from url_shortener.models import UrlModel

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = ("id", "url")

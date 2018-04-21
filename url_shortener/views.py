from url_shortener.serializer import UrlSerializer
from url_shortener.models import UrlModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from url_shortener.hashing import convertUrlToId, convertIdToShortUrl
import traceback

class UrlView(APIView):
    def get(self, request, format = None):
        urlModel = UrlModel.objects.all()
        urlSerializer = UrlSerializer(urlModel, many = True)
        return Response(urlSerializer.data)

    def post(self, request, format = None):
        url = request.data["url"]
        id = convertUrlToId(url)
        shortUrl = convertIdToShortUrl(id)
        data = {
        "id": shortUrl,
        "url": url
        }
        try:
            urlModel = UrlModel.objects.get(id = shortUrl)
            return Response(data, status = status.HTTP_200_OK)
        except Exception as e:
            urlSerializer = UrlSerializer(data = data)
            if(urlSerializer.is_valid()):
             urlSerializer.save()
             return Response(data, status = status.HTTP_200_OK)
            return Response(urlSerializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class UrlDetails(APIView):
    def post(self, request, format = None):
        try:
            print(request.data["id"])
            urlModel = UrlModel.objects.filter(id = request.data["id"])
            urlSerializer = UrlSerializer(urlModel, many = True)
            print(urlSerializer.data)
            return Response({ "url" : urlSerializer.data[0]["url"]}, status = status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            return Response({"id": "not found"}, status = status.HTTP_200_OK)

    def delete(self, request, format = None):
        urlModel = UrlModel.objects.filter(id = request.data["id"])
        urlModel.delete()
        return Response(status = status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from comment_manager.models import CommentManager
from comment_manager.serializer import CommentSerializer

class Comment(APIView):
    
    def get(self, request, format = None):
        commentManager = CommentManager.objects.all()
        if(commentManager):
            serializer = CommentSerializer(commentManager, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({"message": "Entry not found."}, status = status.HTTP_200_OK)
    
    def post(self, request, format = None):
        serializer = CommentSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentDetails(APIView):

    def get(self, request, id, format = None):
        commentManager = CommentManager.objects.filter(id = id)
        if(commentManager):
            serializer = CommentSerializer(commentManager, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({"message": "Entry not found."}, status = status.HTTP_200_OK)
    
    def put(self, request, id, format = None):
        commentManager = CommentManager.objects.get(pk = id)
        if(commentManager):
            serializer = CommentSerializer(commentManager, data = request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": "Entry not found."}, status = status.HTTP_200_OK)
        
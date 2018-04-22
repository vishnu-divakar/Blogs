from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from blog_post.models import BlogPostModel
from blog_post.serializer import BlogPostSerializer

class BlogPost(APIView):

    def get(self, request, format = None):
        blogPostModel = BlogPostModel.objects.all()
        serializer = BlogPostSerializer(blogPostModel, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, format = None):
        serializer = BlogPostSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class BlogPostDetails(APIView):

    def get(self, request, id, format = None):
        blogPostModel = BlogPostModel.objects.filter(id = id)
        if(blogPostModel):
            serializer = BlogPostSerializer(blogPostModel, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({"message": "Entry not found."}, status = status.HTTP_200_OK)
    
    def put(self ,request, id, format = None):
        blogPostModel = BlogPostModel.objects.get(pk = id)
        serializer = BlogPostSerializer(blogPostModel, data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, id, format = None):
        try:
            blogPostModel = BlogPostModel.objects.get(pk = id)
            if(blogPostModel):
                blogPostModel.delete()
                return Response(status = status.HTTP_200_OK)
            return Response({"message": "Entry not found."}, status = status.HTTP_200_OK)
        except BlogPostModel.DoesNotExist:
            return Response({"message": "Entry not found."}, status = status.HTTP_200_OK)


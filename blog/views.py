from django.shortcuts import render
from blog.serializers import BlogSerializer, BlogImageSerializer, ImagesOfBlogSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from blog.models import Blog, BlogImage


# Create your views here.


class BlogPostUploadApiView(APIView):

    def post(self, request, *args, **kwargs):
        blogSerializer = BlogSerializer(data = request.data)
        if blogSerializer.is_valid():
            blog = blogSerializer.save()
            for image in self.request.FILES.getlist('image'):
                blogImageSerializer = BlogImageSerializer(
                    data = {
                        'blog': blog.id,
                        'image': image
                    }
                )
                if blogImageSerializer.is_valid():
                    blogImageSerializer.save()                  
                else:
                    return Response(blogImageSerializer.errors ,status.HTTP_403_FORBIDDEN)
        else:
            return Response(blogImageSerializer.errors ,status.HTTP_403_FORBIDDEN)

        return Response(blogSerializer.data ,status.HTTP_201_CREATED)
                

class BlogListApiView(APIView):

    def get(self, request):
        getBlogs = Blog.objects.all()
        try:
            blogSerializer = BlogSerializer(getBlogs, many=True)
            return Response(blogSerializer.data, status = status.HTTP_200_OK)
        except:
            return Response(blogSerializer.errors ,status.HTTP_403_FORBIDDEN)


class ImagesOfBlogListApiView(APIView):

    def get(self, request, pk):
        getBlog = Blog.objects.get(pk = pk)
        getBlogImages = BlogImage.objects.filter(blog = getBlog.id)
        try:
            imagesOfBlogSerializer = ImagesOfBlogSerializer(getBlogImages, many=True)
            return Response(imagesOfBlogSerializer.data, status = status.HTTP_200_OK)
        except:
            return Response(imagesOfBlogSerializer.errors ,status.HTTP_403_FORBIDDEN)
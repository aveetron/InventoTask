from rest_framework import serializers
from blog.models import Blog, BlogImage



class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = '__all__'


class ImagesOfBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = ['image']
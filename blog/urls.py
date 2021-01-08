from django.urls import path
from blog.views import BlogPostUploadApiView, BlogListApiView, ImagesOfBlogListApiView

urlpatterns = [
    path('api/v0/createBlog/', BlogPostUploadApiView.as_view(), name='blog_post_api'),
    path('api/v0/blogList/', BlogListApiView.as_view(), name='blog_list'),
    path('api/v0/blogImageList/<pk>/',ImagesOfBlogListApiView.as_view(), name='blog_image_list'),
]

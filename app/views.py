from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .serializers import BlogPostSerializers

from .models import BlogPost

class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    http_method_names = ['get','head']
from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .serializers import BlogPostSerializers

from .models import BlogPost

class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [permissions.ALlowAny]
    http_method_names = ['get','head']
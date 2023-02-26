from django.shortcuts import render
from rest_framework import generics

from blogposts.models import BlogPost
from blogposts.serializers import BlogPostSerializer


class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer



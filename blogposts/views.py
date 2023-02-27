from django.shortcuts import render
from rest_framework import generics, permissions

from blogposts.models import BlogPost
from blogposts.permissions import IsAuthorOrReadOnly
from blogposts.serializers import BlogPostSerializer


class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)  # restrict access to authenticated users


class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthorOrReadOnly,)  # restrict access to authenticated users - custom permissions class



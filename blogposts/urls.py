
from django.contrib import admin
from django.urls import path

from blogposts.views import BlogPostList, BlogPostDetail
from books.views import BookListView





urlpatterns = [
    path('v1/<int:pk>/', BlogPostDetail.as_view()),  # root '/api/blogposts/'
    path('v1/', BlogPostList.as_view()),  # root '/api/blogposts/'

]

from django.contrib import admin
from django.urls import path, include

from api.views import BookApiView, TodoList, TodoDetail

urlpatterns = [
    path('todo/<int:pk>/', TodoDetail.as_view()),  # root '/api/'
    path('todo/', TodoList.as_view()),  # root '/api/'
    path('books/', BookApiView.as_view()),  # root '/api/'
]

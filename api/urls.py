
from django.contrib import admin
from django.urls import path, include

from api.views import BookApiView

urlpatterns = [
    path('', BookApiView.as_view()),  # root '/api/'
]

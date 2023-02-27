# custom permission for blogposts: auther can crud, others can read only
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read only for all
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

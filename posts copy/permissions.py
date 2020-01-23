from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Read only allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission are only allowed for the author
        return obj.author == request.user

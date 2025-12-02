from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
        """
        Custom permission to only allow owners of an object to edit it.
        Allows read-only access for other authenticated users.
        """
        def has_object_permission(self, request, view, obj):
            # Read permissions are allowed to any authenticated request,
            # so we'll always allow GET, HEAD or OPTIONS requests.
            if request.method in permissions.SAFE_METHODS:
                return True

            # Write permissions are only allowed to the owner of the snippet.
            return obj.owner == request.user
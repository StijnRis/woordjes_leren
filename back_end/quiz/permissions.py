from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsPublicReadOnly(permissions.BasePermission):
    """
    Allow reading when object in public.
    """

    def has_object_permission(self, request, view, obj):
        visibility = obj.visibility == 'pl'
        safe = request.method in permissions.SAFE_METHODS
        if visibility and safe:
            return True
        return False

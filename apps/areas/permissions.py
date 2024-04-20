# In your app's permissions.py

from rest_framework.permissions import BasePermission


class IsVerified(BasePermission):
    """
    Custom permission to only allow access to verified users.
    """

    def has_permission(self, request, view):
        """
        Check if the user is verified.
        """
        user = request.user
        return user.is_verified

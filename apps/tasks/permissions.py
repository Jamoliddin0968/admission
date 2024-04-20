# In your app's permissions.py

from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    """
    Custom permission to only allow teachers to create, delete, and update tasks.
    """

    def has_permission(self, request, view):
        """
        Check if the user is a teacher.
        """
        return request.user and request.user.is_authenticated and request.user.role == 'teacher'

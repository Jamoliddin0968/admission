# In your app's views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .permissions import IsTeacher
from .serializers import TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated & IsTeacher]


class GetMyTask(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)

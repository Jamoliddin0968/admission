# In your app's urls.py

from django.urls import path

from .views import GetMyTask, TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(),
         name='task-retrieve-update-destroy'),
    path('my-tasks/', GetMyTask.as_view(), name='get-my-tasks'),
]

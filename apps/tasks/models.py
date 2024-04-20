# In your app's models.py

from django.db import models

from apps.accounts.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_file = models.FileField(upload_to='tasks/')
    deadline = models.DateTimeField()

    def __str__(self):
        return f"Task for {self.user.username}"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='answers/')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Answer by {self.user.username} for Task {self.task.id}"

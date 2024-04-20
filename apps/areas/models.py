from django.db import models

# Create your models here.
# In your app's models.py


class EducationalArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class DocumentSubmission(models.Model):
    educational_area = models.ForeignKey(
        EducationalArea, on_delete=models.CASCADE)
    status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"{self.educational_area.name} - {self.status}"

# In your app's views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.areas.permissions import IsVerified

from .models import DocumentSubmission, EducationalArea
from .serializers import (DocumentSubmissionSerializer,
                          EducationalAreaSerializer)


class EducationalAreaListCreate(generics.ListCreateAPIView):
    queryset = EducationalArea.objects.all()
    serializer_class = EducationalAreaSerializer
    permission_classes = [IsAuthenticated, IsVerified,]


class EducationalAreaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationalArea.objects.all()
    serializer_class = EducationalAreaSerializer
    permission_classes = [IsAuthenticated, IsVerified,]
# In your app's views.py


class DocumentSubmissionListCreate(generics.ListCreateAPIView):
    queryset = DocumentSubmission.objects.all()
    serializer_class = DocumentSubmissionSerializer
    permission_classes = [IsAuthenticated, IsVerified,]


class DocumentSubmissionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentSubmission.objects.all()
    serializer_class = DocumentSubmissionSerializer
    permission_classes = [IsAuthenticated, IsVerified,]

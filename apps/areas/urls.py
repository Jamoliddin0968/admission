# In your app's urls.py

from django.urls import path

from .views import (DocumentSubmissionListCreate,
                    DocumentSubmissionRetrieveUpdateDestroy,
                    EducationalAreaListCreate,
                    EducationalAreaRetrieveUpdateDestroy)

urlpatterns = [
    path('educational-areas/', EducationalAreaListCreate.as_view(),
         name='educational-area-list-create'),
    path('educational-areas/<int:pk>/', EducationalAreaRetrieveUpdateDestroy.as_view(),
         name='educational-area-retrieve-update-destroy'),
    path('document-submissions/', DocumentSubmissionListCreate.as_view(),
         name='document-submission-list-create'),
    path('document-submissions/<int:pk>/', DocumentSubmissionRetrieveUpdateDestroy.as_view(),
         name='document-submission-retrieve-update-destroy'),
]

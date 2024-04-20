# In your app's serializers.py

from rest_framework import serializers

from .models import DocumentSubmission, EducationalArea


class EducationalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalArea
        fields = '__all__'


class DocumentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentSubmission
        fields = '__all__'

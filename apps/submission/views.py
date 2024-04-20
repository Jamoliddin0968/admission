from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ContactInfo
from .serializers import ContactInfoSerializer

class ContactInfoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactInfoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user_id = self.kwargs['user_id'] 
        return ContactInfo.objects.filter(user_id=user_id).first()

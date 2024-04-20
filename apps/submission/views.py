from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ContactInfoSerializer, PassportInfoSerializer
from .models import PassportInfo, ContactInfo
class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)
    
class PassportInfoViewSet(viewsets.ModelViewSet):
    queryset = PassportInfo.objects.all()
    serializer_class = PassportInfoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)
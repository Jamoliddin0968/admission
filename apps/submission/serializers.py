from rest_framework.serializers import ModelSerializer
from .models import ContactInfo


class ContactInfoSerializer(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ('id', 'user_id', 'phone_number', 'country',
                    'state', 'city', 'street', 'postal_code')

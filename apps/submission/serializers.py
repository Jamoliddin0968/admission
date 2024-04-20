from rest_framework.serializers import ModelSerializer, ChoiceField
from .models import ContactInfo, PassportInfo, GenderChoices


class ContactInfoSerializer(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ('id', 'user_id', 'phone_number', 'country',
                    'state', 'city', 'street', 'postal_code')


class PassportInfoSerializer(ModelSerializer):
    class Meta:
        model = PassportInfo
        fields = ['id', 'user', 'first_name', 'last_name', 'birthdate', 'gender', 'country', 'district', 'image']

    gender = ChoiceField(choices=GenderChoices.choices)

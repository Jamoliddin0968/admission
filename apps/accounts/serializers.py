# serializers.py
from apps.submission.serializers import ContactInfoSerializer
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    contactinfo = ContactInfoSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'contactinfo']


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)


class OtpCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(min_length=4)

# serializers.py

# serializers.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)


class OtpCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(min_length=6)

# serializers.py


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):

        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email).first()
        if user and not user.check_password(password):
            user = None

        if user:
            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is deactivated')

            data = {}
            refresh = self.get_token(user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return data
        else:
            raise exceptions.AuthenticationFailed(
                'No active account found with the given credentials')

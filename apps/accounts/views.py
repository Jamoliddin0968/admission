import uuid

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.serializers import OtpCodeSerializer, RegistrationSerializer

from .models import OtpCode
from .serializers import CustomTokenObtainPairSerializer
from .utils import generate_otp, send_mail


class RegisterAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        # Generate OTP code
        otp_code = generate_otp()
        username = str(uuid.uuid4())
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user, _ = User.objects.get_or_create(email=email)
        user.username = username
        user.set_password(password)
        user.save()
        OtpCode.objects.create(user=user, otp_code=otp_code)
        send_mail(user.email, otp_code)
        print(User.objects.count())
        return Response({"message": "ok"})


class VerifyEmailAPIView(GenericAPIView):
    # Using the OtpCodeSerializer for validation
    serializer_class = OtpCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        otp_code = serializer.validated_data.get('otp_code')

        try:
            user = User.objects.get(email=email)
            if OtpCode.objects.filter(user=user, otp_code=otp_code).exists():
                user.is_active = True
                user.save()
                refresh = RefreshToken.for_user(user)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP code'}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except OtpCode.DoesNotExist:
            return Response({'error': 'OTP code not found'}, status=status.HTTP_400_BAD_REQUEST)

# views.py


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

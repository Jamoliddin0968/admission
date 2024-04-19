from django.urls import path
from .views import RegisterAPIView, VerifyEmailAPIView
from .views import CustomTokenObtainPairView
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify_email/', VerifyEmailAPIView.as_view(), name='verify_email'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

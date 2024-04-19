from django.urls import path
from .views import RegisterAPIView, VerifyEmailAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify_email/', VerifyEmailAPIView.as_view(), name='verify_email'),
]

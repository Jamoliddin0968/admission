from django.urls import path

from .views import CheckUserStatusView, RegisterAPIView, VerifyEmailAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify-email/', VerifyEmailAPIView.as_view(), name='verify_email'),
    path("check-status/", CheckUserStatusView.as_view())
]

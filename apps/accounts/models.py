# models.py

from django.db import models
from django.contrib.auth.models import User



class OtpCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp_code')
    otp_code = models.CharField(max_length=6)  # Adjust the max_length as needed

    def __str__(self):
        return f"OTP code for {self.user.username}"

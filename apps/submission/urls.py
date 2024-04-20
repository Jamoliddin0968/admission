from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactInfoViewSet

router = DefaultRouter()
router.register(r'contactinfo', ContactInfoViewSet, basename='contactinfo')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

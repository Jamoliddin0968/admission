from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactInfoViewSet, PassportInfoViewSet

router = DefaultRouter()
router.register(r'contactinfo', ContactInfoViewSet, basename='contactinfo')
router.register(r'passportinfo', PassportInfoViewSet, basename='passportinfo')
urlpatterns = [
    path('', include(router.urls)),
]

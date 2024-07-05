from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136220ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136220", Testconnectors136220ViewSet, basename="testconnectors136220"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

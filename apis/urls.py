from django.urls import path
from .views import CandidateViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'candidate', CandidateViewSet, basename='candidate')

urlpatterns = [
] + router.urls

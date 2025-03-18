from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer
from .filters import CandidateSearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CandidateSearchFilter

from django.db.models import Q, Case, When, Value, IntegerField
from .models import Candidate
import django_filters


class CandidateSearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_by_relevancy')

    class Meta:
        model = Candidate
        fields = ['name']

    def filter_by_relevancy(self, queryset, name, value):
        search_terms = value.lower().split()
        q_objects = Q()
        for term in search_terms:
            q_objects |= Q(name__icontains=term)
        queryset = queryset.filter(q_objects)

        match_conditions = [
            Case(
                When(name__icontains=term, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
            for term in search_terms
        ]
        queryset = queryset.annotate(match_count=sum(match_conditions))

        # Sort by match count in descending order
        return queryset.order_by('-match_count')


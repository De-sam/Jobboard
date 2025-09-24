import django_filters as df
from django.db.models import Q
from .models import Job

class JobFilter(df.FilterSet):
    # free-text search on title/description/company
    q = df.CharFilter(method="search")
    category = df.CharFilter(field_name="category__slug", lookup_expr="iexact")
    location = df.CharFilter(field_name="location", lookup_expr="icontains")
    job_type = df.CharFilter(field_name="job_type", lookup_expr="iexact")
    is_active = df.BooleanFilter(field_name="is_active")

    class Meta:
        model = Job
        fields = ["category", "location", "job_type", "is_active"]

    def search(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(company__icontains=value)
        )

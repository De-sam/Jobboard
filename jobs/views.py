from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Category, Job, Application
from .serializers import CategorySerializer, JobSerializer, ApplicationSerializer

# If you created jobs/filters.py & jobs/pagination.py, we can use them:
# - JobFilter gives ?q= free-text + slug-based category filter
try:
    from .filters import JobFilter
    HAS_JOB_FILTER = True
except Exception:
    HAS_JOB_FILTER = False


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    SAFE_METHODS = read for anyone.
    Mutations (POST/PATCH/DELETE) require is_staff.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


@extend_schema_view(
    list=extend_schema(tags=["Categories"]),
    retrieve=extend_schema(tags=["Categories"]),
    create=extend_schema(tags=["Categories"]),
    partial_update=extend_schema(tags=["Categories"]),
    destroy=extend_schema(tags=["Categories"]),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"


@extend_schema_view(
    list=extend_schema(tags=["Jobs"]),
    retrieve=extend_schema(tags=["Jobs"]),
    create=extend_schema(tags=["Jobs"]),
    partial_update=extend_schema(tags=["Jobs"]),
    destroy=extend_schema(tags=["Jobs"]),
)
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related("category").all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminOrReadOnly]

    # Prefer dedicated filter class if present (adds ?q= & cleaner params)
    if HAS_JOB_FILTER:
        from .filters import JobFilter  # type: ignore
        filterset_class = JobFilter
    else:
        # Fallback: basic filter fields (works without filters.py)
        filterset_fields = ["category__slug", "location", "job_type", "is_active"]

    search_fields = ["title", "description", "company", "location"]
    ordering_fields = ["created_at", "title", "location"]
    ordering = ["-created_at"]

    @extend_schema(tags=["Jobs"])
    @action(detail=False, methods=["get"], url_path="active")
    def active(self, request):
        qs = self.filter_queryset(self.get_queryset().filter(is_active=True))
        page = self.paginate_queryset(qs)
        if page is not None:
            return self.get_paginated_response(self.get_serializer(page, many=True).data)
        return Response(self.get_serializer(qs, many=True).data)


@extend_schema_view(
    list=extend_schema(tags=["Applications"]),
    retrieve=extend_schema(tags=["Applications"]),
    create=extend_schema(tags=["Applications"]),
)
class ApplicationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Application.objects.select_related("job", "user").all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(user=user)

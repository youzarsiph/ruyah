""" API views for task_flow.categories """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from task_flow.categories.models import Category
from task_flow.categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    """Category API endpoints"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at" "updated_at"]

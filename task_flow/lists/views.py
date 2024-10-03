""" API endpoints for tasks.lists """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from task_flow.lists.models import List
from task_flow.lists.serializers import ListSerializer
from task_flow.mixins import OwnerMixin
from task_flow.permissions import IsOwner


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete task lists"""

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at" "updated_at"]

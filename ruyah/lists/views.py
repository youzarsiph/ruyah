""" API endpoints for tasks.lists """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ruyah.lists.models import List
from ruyah.lists.serializers import ListRetrieveSerializer, ListSerializer
from ruyah.mixins import OwnerMixin
from ruyah.permissions import IsOwner


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete task lists"""

    queryset = List.objects.prefetch_related("tasks")
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at" "updated_at"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "retrieve":
            self.serializer_class = ListRetrieveSerializer

        return super().get_serializer(*args, **kwargs)

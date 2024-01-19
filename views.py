""" API endpoints for tasks """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.mixins import OwnerMixin
from tasks.models import List, Task
from tasks.permissions import IsOwner
from tasks.serializers import ListSerializer, TaskSerializer


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete task lists"""

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at" "updated_at"]
    filterset_fields = ["name"]


class TaskViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete tasks"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["title", "description", "deadline"]
    filterset_fields = ["list", "title", "is_completed", "is_starred", "deadline"]
    ordering_fields = [
        "title",
        "deadline",
        "is_starred",
        "is_completed",
        "created_at",
        "updated_at",
    ]


class ListTasksViewSet(TaskViewSet):
    """Tasks of a task list"""

    def get_queryset(self):
        """Filter queryset by list"""

        list = List.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(list=list)

    def perform_create(self, serializer):
        """Adds a task to a task list"""

        list = List.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, list=list)

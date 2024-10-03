""" API endpoints for task_flow.tasks """

from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from task_flow.mixins import OwnerMixin
from task_flow.permissions import IsOwner
from task_flow.tasks.models import Task
from task_flow.tasks.serializers import TaskSerializer


# Create your views here.
class TaskViewSet(OwnerMixin, ModelViewSet):
    """Task API endpoints"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "deadline", "priority", "created_at", "updated_at"]
    filterset_fields = [
        "category",
        "list",
        "tags",
        "progress",
        "priority",
        "is_starred",
        "is_completed",
        "deadline",
    ]

    @action(detail=True, methods=["POST"])
    def star(self, request: Request, pk: int) -> Response:
        """Marks a task as starred"""

        task = self.get_object()
        task.is_starred = not task.is_starred
        task.save()

        return Response(
            {
                "details": f"Task {task.id} {'added to' if task.is_starred else 'removed from'} starred tasks"
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["POST"])
    def check(self, request: Request, pk: int) -> Response:
        """Marks a task as completed"""

        task = self.get_object()
        task.is_completed = not task.is_completed
        task.save()

        return Response(
            {
                "details": f"Task {task.id} {'added to' if task.is_completed else 'removed from'} completed tasks"
            },
            status=status.HTTP_200_OK,
        )

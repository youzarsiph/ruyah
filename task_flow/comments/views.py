""" API endpoints for tasks.Comments """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from task_flow.comments.models import Comment
from task_flow.comments.serializers import CommentSerializer
from task_flow.mixins import OwnerMixin
from task_flow.permissions import IsOwner


# Create your views here.
class CommentViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete task comments"""

    queryset = Comment.objects.prefetch_related("task")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = ["task"]
    search_fields = ["content"]
    ordering_fields = ["created_at" "updated_at"]

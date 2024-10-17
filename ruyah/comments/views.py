""" API endpoints for tasks.Comments """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ruyah.comments.models import Comment
from ruyah.comments.serializers import CommentSerializer
from ruyah.mixins import OwnerMixin
from ruyah.permissions import IsOwner


# Create your views here.
class CommentViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete task comments"""

    queryset = Comment.objects.prefetch_related("task")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = ["task"]
    search_fields = ["content"]
    ordering_fields = ["created_at" "updated_at"]

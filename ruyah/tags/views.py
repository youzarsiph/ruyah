""" API views for ruyah.tags """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ruyah.tags.models import Tag
from ruyah.tags.serializers import TagSerializer


# Create your views here.
class TagViewSet(ModelViewSet):
    """Tag API endpoints"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at" "updated_at"]

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]

        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()

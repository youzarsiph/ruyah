""" Serializers for task_flow.tags """

from rest_framework.serializers import ModelSerializer

from task_flow.tags.models import Tag


# Create your serializers here.
class TagSerializer(ModelSerializer):
    """Task Tag Serializer"""

    class Meta:
        """Meta data"""

        model = Tag
        fields = [
            "id",
            "url",
            "name",
            "description",
            "task_count",
            "created_at",
            "updated_at",
        ]

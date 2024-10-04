""" Serializers for task_flow.tasks """

from rest_framework.serializers import ModelSerializer
from task_flow.tasks.models import Task


# Create your serializers here.
class TaskSerializer(ModelSerializer):
    """Task Serializer"""

    class Meta:
        """Meta data"""

        depth = 1
        model = Task
        read_only_fields = ["progress"]
        fields = [
            "id",
            "url",
            "list",
            "category",
            "title",
            "description",
            "deadline",
            "priority",
            "progress",
            "is_starred",
            "is_completed",
            "tags",
            "created_at",
            "updated_at",
        ]

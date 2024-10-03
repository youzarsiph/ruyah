""" Serializers for task_flow.tasks """

from rest_framework.serializers import ModelSerializer
from task_flow.tasks.models import Task


# Create your serializers here.
class TaskSerializer(ModelSerializer):
    """Task Serializer"""

    class Meta:
        """Meta data"""

        model = Task
        read_only_fields = ["user", "list"]
        fields = [
            "id",
            "url",
            "user",
            "list",
            "title",
            "description",
            "deadline",
            "priority",
            "progress",
            "is_starred",
            "is_completed",
            "created_at",
            "updated_at",
        ]

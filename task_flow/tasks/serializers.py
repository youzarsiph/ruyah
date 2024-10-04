""" Serializers for task_flow.tasks """

from rest_framework.serializers import ModelSerializer
from task_flow.tasks.models import Task


# Create your serializers here.
class TaskSerializer(ModelSerializer):
    """Task Serializer"""

    class Meta:
        """Meta data"""

        model = Task
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
            "comments",
            "tags",
            "subtasks",
            "created_at",
            "updated_at",
        ]


class TaskRetrieveSerializer(TaskSerializer):
    """Task serializer for retrieve action"""

    class Meta(TaskSerializer.Meta):
        """Meta data"""

        depth = 1

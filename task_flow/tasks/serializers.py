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
            "category",
            "list",
            "title",
            "description",
            "attachment",
            "is_completed",
            "is_starred",
            "deadline",
            "priority",
            "progress",
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

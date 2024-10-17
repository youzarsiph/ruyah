""" Serializers for ruyah.tasks """

from rest_framework.serializers import ModelSerializer
from ruyah.tasks.models import Task


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
            "is_recurring",
            "recurrence_type",
            "recurrence_interval",
            "recurrence_start_date",
            "recurrence_end_date",
            "occurrence_count",
            "created_at",
            "updated_at",
        ]


class TaskRetrieveSerializer(TaskSerializer):
    """Task serializer for retrieve action"""

    class Meta(TaskSerializer.Meta):
        """Meta data"""

        depth = 1

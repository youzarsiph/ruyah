""" Serializers """


from rest_framework.serializers import ModelSerializer
from tasks.models import List, Task


# Create your serializers here.
class ListSerializer(ModelSerializer):
    """Task List Serializer"""

    class Meta:
        """Meta data"""

        model = List
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "name",
            "description",
            "progress",
            "task_count",
            "created_at",
            "updated_at",
        ]


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
            "progress",
            "is_starred",
            "is_completed",
            "created_at",
            "updated_at",
        ]

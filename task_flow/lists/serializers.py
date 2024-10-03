""" Serializers for task_flow.lists """

from rest_framework.serializers import ModelSerializer

from lists.models import List


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

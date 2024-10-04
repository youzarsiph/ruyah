""" Serializers for task_flow.lists """

from rest_framework.serializers import ModelSerializer

from task_flow.lists.models import List


# Create your serializers here.
class ListSerializer(ModelSerializer):
    """Task List Serializer"""

    class Meta:
        """Meta data"""

        model = List
        fields = [
            "id",
            "url",
            "name",
            "description",
            "progress",
            "task_count",
            "created_at",
            "updated_at",
        ]


class ListRetrieveSerializer(ListSerializer):
    """Task List Serializer for retrieve action"""

    class Meta:
        """Meta data"""

        depth = 1
        fields = ListSerializer.Meta.fields + ["tasks"]

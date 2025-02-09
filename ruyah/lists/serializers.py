""" Serializers for ruyah.lists """

from rest_framework.serializers import ModelSerializer

from ruyah.lists.models import List


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

    class Meta(ListSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = ListSerializer.Meta.fields + ["tasks"]

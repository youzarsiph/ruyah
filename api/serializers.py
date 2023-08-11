""" Serializers """


from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from tasks.models import List, Task


# Create your serializers here.
class HyperlinkedListSerializer(HyperlinkedModelSerializer):
    """Task List Serializer"""

    class Meta:
        """Meta data"""

        model = List
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]


class HyperlinkedTaskSerializer(HyperlinkedModelSerializer):
    """Task Serializer"""

    class Meta:
        """Meta data"""

        model = Task
        fields = [
            "id",
            "url",
            "title",
            "description",
            "completion_rate",
            "completed",
            "starred",
            "deadline",
            "created_at",
            "updated_at",
        ]


class TaskSerializer(ModelSerializer):
    """Task Serializer"""

    class Meta:
        """Meta data"""

        depth = 1
        model = Task
        fields = [
            "id",
            "list",
            "title",
            "description",
            "completion_rate",
            "completed",
            "starred",
            "deadline",
            "created_at",
            "updated_at",
        ]

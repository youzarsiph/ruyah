""" Serializers for task_flow.categories """

from rest_framework.serializers import ModelSerializer

from task_flow.categories.models import Category


# Create your serializers here.
class CategorySerializer(ModelSerializer):
    """Task Category Serializer"""

    class Meta:
        """Meta data"""

        model = Category
        fields = [
            "id",
            "url",
            "name",
            "description",
            "task_count",
            "created_at",
            "updated_at",
        ]

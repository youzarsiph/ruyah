""" Serializers for ruyah.categories """

from rest_framework.serializers import ModelSerializer

from ruyah.categories.models import Category


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

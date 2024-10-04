""" Serializers for task_flow.comments """

from rest_framework.serializers import ModelSerializer

from task_flow.comments.models import Comment


# Create your serializers here.
class CommentSerializer(ModelSerializer):
    """Task Comment Serializer"""

    class Meta:
        """Meta data"""

        model = Comment
        fields = [
            "id",
            "url",
            "task",
            "content",
            "created_at",
            "updated_at",
        ]

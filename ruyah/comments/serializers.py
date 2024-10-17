""" Serializers for ruyah.comments """

from rest_framework.serializers import ModelSerializer

from ruyah.comments.models import Comment


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
            "attachment",
            "created_at",
            "updated_at",
        ]

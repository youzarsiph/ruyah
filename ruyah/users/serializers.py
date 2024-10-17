""" Serializers for ruyah.users """

from rest_framework.serializers import ModelSerializer

from ruyah.users.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = [
            "id",
            "image",
            "username",
            "first_name",
            "last_name",
            "task_count",
        ]

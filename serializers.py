""" Serializers """


from rest_framework.serializers import ModelSerializer
from tasks.models import List, Task


# Create your serializers here.
class ListSerializer(ModelSerializer):
    """ Serializer """

    class Meta:
        """ Meta data """

        model = List
        fields = ['id', 'user', 'name', 'default', 'created_at', 'updated_at']


class TaskSerializer(ModelSerializer):
    """ Serializer """

    class Meta:
        """ Meta data """

        model = Task
        fields = [
            'id', 'user', 'list', 'title', 'description',
            'completed', 'starred', 'due', 'created_at', 'updated_at'
        ]

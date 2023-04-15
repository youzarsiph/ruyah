""" Serializers """


from rest_framework.serializers import ModelSerializer
from tasks.models import List, Task


# Create your serializers here.
class ListSerializer(ModelSerializer):
    """ Task List Serializer """

    class Meta:
        """ Meta data """

        model = List
        fields = ['id', 'name', 'default', 'created_at', 'updated_at']


class TaskSerializer(ModelSerializer):
    """ Task Serializer """

    class Meta:
        """ Meta data """

        model = Task
        fields = [
            'id', 'title', 'description',
            'completed', 'starred', 'due', 'created_at', 'updated_at'
        ]

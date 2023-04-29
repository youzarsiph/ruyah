""" Serializers """


from rest_framework.serializers import HyperlinkedModelSerializer
from tasks.models import List, Task


# Create your serializers here.
class ListSerializer(HyperlinkedModelSerializer):
    """ Task List Serializer """

    class Meta:
        """ Meta data """

        model = List
        fields = [
            'id', 'url', 'name', 'description',
            'default', 'created_at', 'updated_at'
        ]


class TaskSerializer(HyperlinkedModelSerializer):
    """ Task Serializer """

    class Meta:
        """ Meta data """

        model = Task
        fields = [
            'id', 'url', 'title', 'description',
            'completed', 'starred', 'due', 'created_at', 'updated_at'
        ]


class TaskSerializerWithList(TaskSerializer):
    """ Task Serializer """

    class Meta(TaskSerializer.Meta):
        """ Meta data """

        fields = [
            'id', 'url', 'list', 'title', 'description',
            'completed', 'starred', 'due', 'created_at', 'updated_at'
        ]

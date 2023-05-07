""" ViewSets """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from tasks import serializers
from tasks.mixins import OwnerMixin
from tasks.models import List, Task
from tasks.permissions import OwnerPermission


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """ A ViewSet for performing CRUD operations on List model """

    queryset = List.objects.all()
    serializer_class = serializers.ListSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'default']
    filterset_fields = ['name', 'default']


class TaskViewSet(OwnerMixin, ModelViewSet):
    """ A ViewSet for performing CRUD operations on Task model """

    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializerWithList
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['title', 'description', 'due']
    ordering_fields = ['title', 'completed', 'starred', 'due']
    filterset_fields = ['title', 'completed', 'starred', 'due']


class ListTasksViewSet(TaskViewSet):
    """ A ViewSet for performing CRUD operations on Task model """

    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        """ Filter tasks by list """

        # Get list instance
        lst = List.objects.get(id=self.kwargs['id'])

        return super().get_queryset().filter(list=lst)

    def perform_create(self, serializer):
        """ Add list instance before saving """

        lst = List.objects.get(id=self.kwargs['id'])

        serializer.save(user=self.request.user, list=lst)

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
    """ A ViewSet that allows the user to create, read, update and delete their task lists. """

    queryset = List.objects.all()
    serializer_class = serializers.HyperlinkedListSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['name', 'description']
    ordering_fields = ['name', ]
    filterset_fields = ['name', ]


class TaskViewSet(OwnerMixin, ModelViewSet):
    """ A ViewSet that allows the user to crete, read, update and delete their tasks """

    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['title', 'description', 'deadline']
    ordering_fields = ['title', 'completed', 'starred', 'deadline']
    filterset_fields = ['title', 'completed', 'starred', 'deadline']


class ListTasksViewSet(TaskViewSet):
    """ A ViewSet that allows the user to crete, read, update and delete their tasks """

    serializer_class = serializers.HyperlinkedTaskSerializer

    def get_queryset(self):
        """ Filter tasks by list """

        # Get list instance
        lst = List.objects.get(id=self.kwargs['id'])

        return super().get_queryset().filter(list=lst)

    def perform_create(self, serializer):
        """ Add list instance before saving """

        lst = List.objects.get(id=self.kwargs['id'])

        serializer.save(user=self.request.user, list=lst)

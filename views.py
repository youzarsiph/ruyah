""" ViewSets """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from tasks.mixins import OwnerMixin
from tasks.models import List, Task
from tasks.permissions import OwnerPermission
from tasks.serializers import ListSerializer, TaskSerializer


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """ ListViewSet for Creating, reading, updating and deleting task lists """

    queryset = List.objects.all()
    serializer_class = ListSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['name', ]
    ordering_fields = ['name', 'default']
    filterset_fields = ['name', 'default']


class TaskViewSet(OwnerMixin, ModelViewSet):
    """ TaskViewSet for Creating, reading, updating and deleting tasks """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'completed', 'starred']
    filterset_fields = ['title', 'completed', 'starred']


class UserTasksViewSet(TaskViewSet):
    """ UserTasksViewSet for Creating, reading, updating and deleting tasks """

    def get_queryset(self):
        """ Filter tasks by list """

        # Get list instance
        lst = List.objects.get(id=self.kwargs['id'])

        return super().get_queryset().filter(list=lst)

    def perform_create(self, serializer):
        """ Add list instance before saving """

        lst = List.objects.get(id=self.kwargs['id'])

        serializer.save(user=self.request.user, list=lst)

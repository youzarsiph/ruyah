""" Views """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from tasks.mixins import OwnerMixin
from tasks.models import List, Task
from tasks.permissions import OwnerPermission
from tasks.serializers import ListSerializer, TaskSerializer


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """ ListViewSet to create, read, update and delete task lists """

    queryset = List.objects.all()
    serializer_class = ListSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['name', ]
    filterset_fields = ['default', ]
    ordering_fields = ['id', 'name', 'default', ]


class TaskViewSet(OwnerMixin, ModelViewSet):
    """ TaskViewSet to create, read, update and delete tasks """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated, OwnerPermission]
    search_fields = ['title', 'description']
    filterset_fields = ['completed', 'starred']
    ordering_fields = ['id', 'title', 'completed', 'starred']

    def get_queryset(self):
        """ Filter tasks """

        # Get list instance
        lst = List.objects.get(id=self.kwargs['id'])

        return super().get_queryset().filter(list=lst)

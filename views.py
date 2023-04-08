""" Views """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.mixins import OwnerMixin
from tasks.models import List, Task
from tasks.permissions import OwnerPermission
from tasks.serializers import ListSerializer, TaskSerializer


# Create your views here.
class ListViewSet(OwnerMixin, ModelViewSet):
    """ View Set """

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated, OwnerPermission]


class TaskViewSet(OwnerMixin, ModelViewSet):
    """ View Set """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Filter tasks """

        # Get list instance
        lst = List.objects.get(id=self.kwargs['id'])

        return super().get_queryset().filter(list=lst)

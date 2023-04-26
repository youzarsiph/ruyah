""" URLConf for tasks """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import ListViewSet, TaskViewSet, UserTasksViewSet


# Create your routers here.
router = DefaultRouter(trailing_slash=False)
router.register('lists', ListViewSet, 'list')
router.register('tasks', TaskViewSet, 'task')


# Create your patters here.
urlpatterns = [
    path('', include(router.urls)),

    # List tasks
    path('lists/<int:id>/tasks/', UserTasksViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('lists/<int:id>/tasks/<int:pk>/', UserTasksViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]

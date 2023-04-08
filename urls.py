""" URLConf for tasks """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import ListViewSet, TaskViewSet


# Create your routers here.
router = DefaultRouter(trailing_slash=False)
router.register('lists', ListViewSet)


# Create your patters here.
urlpatterns = [
    path('', include(router.urls)),

    # List tasks
    path('lists/<int:id>/tasks/', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('lists/<int:id>/tasks/<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]

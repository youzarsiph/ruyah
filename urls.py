""" URLConf for tasks """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import ListViewSet, TaskViewSet, ListTasksViewSet


# Create your routers here.
router = DefaultRouter(trailing_slash=False)
router.register("lists", ListViewSet, "list")
router.register("tasks", TaskViewSet, "task")

sub_router = DefaultRouter()
sub_router.register("tasks", ListTasksViewSet, "task")

# Create your patters here.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "lists/<int:id>/",
        include((sub_router.urls, "lists"), namespace="lists"),
    ),
]

""" URLConf for task_flow """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task_flow.categories.views import CategoryViewSet
from task_flow.lists.views import ListViewSet
from task_flow.tags.views import TagViewSet
from task_flow.tasks.views import TaskViewSet


# Create your routers here.
router = DefaultRouter(trailing_slash=False)
router.register("categories", CategoryViewSet, "category")
router.register("lists", ListViewSet, "list")
router.register("tags", TagViewSet, "tag")
router.register("tasks", TaskViewSet, "task")

# Create your patters here.
urlpatterns = [
    path("", include(router.urls)),
]

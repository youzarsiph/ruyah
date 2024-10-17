""" URLConf for ruyah """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ruyah.categories.views import CategoryViewSet
from ruyah.comments.views import CommentViewSet
from ruyah.lists.views import ListViewSet
from ruyah.tags.views import TagViewSet
from ruyah.tasks.views import TaskViewSet


# Create your routers here.
router = DefaultRouter(trailing_slash=False)
router.register("categories", CategoryViewSet, "category")
router.register("comments", CommentViewSet, "comment")
router.register("lists", ListViewSet, "list")
router.register("tags", TagViewSet, "tag")
router.register("tasks", TaskViewSet, "task")

# Create your patters here.
urlpatterns = [
    path("", include(router.urls)),
]

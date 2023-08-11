""" Views """


from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import User, List, Task
from tasks.mixins import AccountOwnerMixin, UserFilterMixin, SaveWithUserMixin


# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView):
    """Home"""

    template_name = "tasks/index.html"


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """Profile"""

    template_name = "tasks/profile.html"


# Users
class UserCreateView(SuccessMessageMixin, generic.CreateView):
    """Creates a user"""

    model = User
    form_class = UserCreationForm
    template_name = "tasks/user_form.html"
    success_url = reverse_lazy("tasks:profile")
    success_message = "Your account created successfuly!"


class UserUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    AccountOwnerMixin,
    generic.UpdateView
):
    """Updates a user"""

    model = User
    template_name = "tasks/user_form.html"
    success_url = reverse_lazy("tasks:profile")
    success_message = "Your account updated successfuly!"
    fields = ["username", "first_name", "last_name", "email"]


class UserDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    AccountOwnerMixin,
    generic.DeleteView
):
    """Deletes a user"""

    model = User
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/user_confirm_delete.html"
    success_message = "Your account deleted successfuly!"


# Lists
class ListCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    SaveWithUserMixin,
    generic.CreateView
):
    """Creates a task list"""

    model = List
    fields = ["name", "description"]
    success_url = reverse_lazy("tasks:lists")
    success_message = "List created successfuly!"


class ListView(LoginRequiredMixin, UserFilterMixin, generic.ListView):
    """Displays task lists"""

    model = List


class ListDetailView(LoginRequiredMixin, UserFilterMixin, generic.DetailView):
    """Displays a task list"""

    model = List


class ListUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UserFilterMixin,
    generic.UpdateView
):
    """Updates a task list"""

    model = List
    fields = ["name", "description"]
    success_url = reverse_lazy("tasks:lists")
    success_message = "List updated successfuly!"


class ListDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UserFilterMixin,
    generic.DeleteView
):
    """Deletes a task list"""

    model = List
    success_url = reverse_lazy("tasks:lists")
    success_message = "List deleted successfuly!"


# Tasks
class BaseTaskView:
    """Overrides get_success_url"""

    def get_success_url(self):
        """Return success_url"""

        return reverse_lazy("tasks:list_detail", args=[self.object.list.pk])


class StarredTasksView(LoginRequiredMixin, generic.TemplateView):
    """Displays starred tasks"""

    template_name = "tasks/starred.html"


class CompletedTasksView(LoginRequiredMixin, generic.TemplateView):
    """Displays starred tasks"""

    template_name = "tasks/completed.html"


class TaskCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    SaveWithUserMixin,
    BaseTaskView,
    generic.CreateView,
):
    """Creates a task"""

    model = Task
    success_message = "Task created successfuly!"
    fields = [
        "list",
        "title",
        "description",
        "completed",
        "starred",
        "deadline",
        "completion_rate",
    ]


class TaskDetailView(LoginRequiredMixin, UserFilterMixin, generic.DetailView):
    """Displays a task"""

    model = Task


class TaskUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UserFilterMixin,
    BaseTaskView,
    generic.UpdateView,
):
    """Updates a task"""

    model = Task
    success_message = "Task updated successfuly!"
    fields = [
        "title",
        "description",
        "completed",
        "starred",
        "deadline",
        "completion_rate",
    ]


class TaskDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UserFilterMixin,
    generic.DeleteView
):
    """Deletes a task"""

    model = Task
    success_url = reverse_lazy("tasks:index")
    success_message = "Task deleted successfuly!"

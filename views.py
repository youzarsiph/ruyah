""" Views """


from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import User, List, Task
from tasks.mixins import AccountOwnerMixin, UserFilterMixin, SaveWithUserMixin


# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView):
    """ Home """

    template_name = 'tasks/index.html'


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """ Profile """

    template_name = 'tasks/profile.html'


# Users
class UserCreateView(LoginRequiredMixin, generic.CreateView):
    """ Creates a user """

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks:profile')


class UserUpdateView(LoginRequiredMixin, AccountOwnerMixin, generic.UpdateView):
    """ Updates a user """

    model = User
    success_url = reverse_lazy('tasks:profile')
    fields = ['username', 'first_name', 'last_name', 'email']


class UserDeleteView(LoginRequiredMixin, AccountOwnerMixin, generic.DeleteView):
    """ Deletes a user """

    model = User
    success_url = reverse_lazy('tasks:index')


# Lists
class ListCreateView(LoginRequiredMixin, SaveWithUserMixin, generic.CreateView):
    """ Creates a task list """

    model = List
    fields = ['name', 'description']
    success_url = reverse_lazy('tasks:lists')


class ListView(LoginRequiredMixin, UserFilterMixin, generic.ListView):
    """ Displays task lists """

    model = List


class ListDetailView(LoginRequiredMixin, UserFilterMixin, generic.DetailView):
    """ Displays a task list """

    model = List


class ListUpdateView(LoginRequiredMixin, UserFilterMixin, generic.UpdateView):
    """ Updates a task list """

    model = List
    fields = ['name', 'description']
    success_url = reverse_lazy('tasks:lists')


class ListDeleteView(LoginRequiredMixin, UserFilterMixin, generic.DeleteView):
    """ Deletes a task list """

    model = List
    success_url = reverse_lazy('tasks:lists')


# Tasks
class BaseTaskView:
    """ Overrides get_success_url """

    def get_success_url(self):
        """ Return success_url """

        return reverse_lazy('tasks:list_detail', args=[self.object.list.pk])


class TaskCreateView(LoginRequiredMixin, SaveWithUserMixin, BaseTaskView, generic.CreateView):
    """ Creates a task """

    model = Task
    fields = ['list', 'title', 'description', 'completed', 'starred', 'deadline', 'completion_rate']


class TaskDetailView(LoginRequiredMixin, UserFilterMixin, generic.DetailView):
    """ Displays a task """

    model = Task


class TaskUpdateView(LoginRequiredMixin, UserFilterMixin, BaseTaskView, generic.UpdateView):
    """ Updates a task """

    model = Task
    fields = ['title', 'description', 'completed', 'starred', 'deadline', 'completion_rate']


class TaskDeleteView(LoginRequiredMixin, UserFilterMixin, BaseTaskView, generic.DeleteView):
    """ Deletes a task """

    model = Task
    success_url = reverse_lazy('tasks:index')

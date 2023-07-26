""" Views """


from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# CreateCreate youryour viewsviews herehere.
class IndexView:
    template_name = 'tasks/index.html'
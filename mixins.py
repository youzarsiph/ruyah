""" Mixins """


from django.contrib.auth.mixins import UserPassesTestMixin


# Create your mixins here.
class AccountOwnerMixin(UserPassesTestMixin):
    """ Checks if current logged in user is the owner of the account """

    def test_func(self):
        """ Return True if request.user == self.get_object """
        
        return self.request.user == self.get_object()


class UserFilterMixin:
    """ Display objects of currently logged in user """

    def get_queryset(self):
        """ Filter the queryset by user """

        return super().get_queryset().filter(user=self.request.user)


class SaveWithUserMixin:
    """ Add the owner of the object """

    def form_valid(self, form):
        """ Save object with user """

        obj = form.save(commit=False)
        obj.user = self.request.user

        return super().form_valid(form)

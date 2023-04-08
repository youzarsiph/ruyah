""" Mixins """


from rest_framework.permissions import IsAuthenticated


# Create your mixins here.
class OwnerMixin:
    """ Adds object's owner """

    def perform_create(self, serializer):
        """ Add object's owner """

        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Return only objects of current logged in user """

        return super().get_queryset().filter(user=self.request.user)

    def get_permissions(self):
        """ Permissions based on self.action """

        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

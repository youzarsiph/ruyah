""" Mixins """


# Create your mixins here.
class OwnerMixin:
    """Allow owners only"""

    def perform_create(self, serializer):
        """Add object's owner"""

        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Return only objects of current logged in user"""

        return super().get_queryset().filter(user=self.request.user)

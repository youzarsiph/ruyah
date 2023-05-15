""" Task models """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class List(models.Model):
    """ Task Lists """

    # The owner of the list
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=32,
        db_index=True,
        help_text='List name'
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Task list description'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta data """

        db_table = 'list'

    def __str__(self):
        return self.name


class Task(models.Model):
    """ Tasks """

    # The owner of the list
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # The list that the task belongs to
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=32,
        db_index=True,
        help_text='Task title'
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Task description'
    )
    completed = models.BooleanField(
        default=False,
        help_text='Designates if the task is completed'
    )
    starred = models.BooleanField(
        default=False,
        help_text='Designates if the task is important'
    )
    due = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Due date'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta data """

        db_table = 'task'

    def __str__(self):
        return self.title

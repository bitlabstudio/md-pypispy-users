"""Models for the ``md-pypispy-users`` app."""
from django.db import models


class UserCount(models.Model):
    """
    The number of pypispy.com users at a given time.

    :creation_date: The datetime when the data entry has been made.
    :value: The number of users at the given time.

    """
    creation_date = models.DateTimeField()
    value = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.value)

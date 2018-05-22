from django.db import models
from apps.user.models import People


class Teacher(People):
    """
    Model for Teacher Type
    """
    root = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

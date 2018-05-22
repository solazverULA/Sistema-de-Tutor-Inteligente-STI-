from django.db import models
from apps.user.models import People


class Student(People):
    """
    Model for Student Type
    """
    progress = models.CharField(max_length=10)
    teacherMentor = models.ForeignKey('user.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

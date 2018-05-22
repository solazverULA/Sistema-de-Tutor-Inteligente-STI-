from django.db import models
from apps.user.models import People
from apps.teacher.models import Teacher


class Student(People):
    """
    Model for Student Type
    """
    progress = models.CharField(max_length=10)
    teacherMentor = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

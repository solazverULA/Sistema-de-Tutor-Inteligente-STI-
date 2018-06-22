from django.db import models
from apps.user.models import People
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.teacher.models import Teacher


class Student(People):
    """
    Model for Student Type
    """
    progress = models.CharField(max_length=10, blank=True, null=True)
    teacherMentor = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Student)
def update_student_profile(sender, instance, created, **kwargs):
    if created:
        # Student.objects.create(user=instance)
        for theme in Theme.objects.all():
            learning = LearningTheme.objects.create(student=instance,
                                                    theme=theme, ready=False)
            learning.save()


class Theme(models.Model):
    """
    Model for Theme Type
    """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400, null=True, blank=True)
    initial_address = models.CharField(max_length=300, null=True, blank=True)
    referenceContent = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Theme)
def update_student_profile(sender, instance, created, **kwargs):
    if created:
        # Student.objects.create(user=instance)
        for student in Student.objects.all():
            learning = LearningTheme.objects.create(student=student,
                                                    theme=instance, ready=False)
            learning.save()


class Problem(models.Model):
    """
    Model for Problem Type
    """
    title = models.CharField(max_length=150)
    difficult = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    # referenceInput = models.FileField(upload_to='uploads/')
    referenceOutput = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title


class LearningTheme(models.Model):
    """
    Model for Learning Theme Type
    """
    class Meta:
        unique_together = (('student', 'theme'),)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.student.user.username + " " + self.theme.name


class MakingProblem(models.Model):
    """
    Model for Making Problem Type
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return self.student.user.username + " " + self.problem.title

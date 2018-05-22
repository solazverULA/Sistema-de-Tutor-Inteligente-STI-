from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class People(models.Model):
    """
    Model for User Type
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.CharField(max_length=10, unique=True,
                          validators=[RegexValidator
                                      (regex="^[0-9]{10}$",
                                       message="Invalid format for CI")])
    profileImage = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.user.username

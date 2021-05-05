from django.contrib.auth.models import AbstractUser
from django.db import models

# User model.
class User(AbstractUser):
    pass

# Record model
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    seconds = models.IntegerField()
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
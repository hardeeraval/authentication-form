from django.db import models
from django.contrib.auth.models import User

class aut(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

# Create your models here.

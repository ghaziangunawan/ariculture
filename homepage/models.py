from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()